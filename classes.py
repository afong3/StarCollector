# Testing for activity class
from gpxpy import gpx
from global_functions import gpx_to_lat_lon_list, fit_points_to_bounds, match_maps
import os
import numpy as np 
import requests
import datetime
import calendar
import pandas as pd

class Athlete:
    def __init__(self, clientId, clientSecret, refreshToken, athleteId):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.refreshToken = refreshToken
        self.athleteId = athleteId


    # retrieve the access token from strava, assign auth token to self.accessToken. Scope: activity:read_all. User must do the funky requests to get the correct refresh token
    def retrieveAuthToken(self):
        params1 = {'client_id': self.clientId, 'client_secret': self.clientSecret, 'grant_type':"refresh_token", 'refresh_token': self.refreshToken}
        response = requests.post("https://www.strava.com/oauth/token", params = params1)
        print("Response1: {token}".format(token = response))
        response_json = response.json()
        access_token = response_json["access_token"] #access tokens expire every six hours
        self.accessToken = access_token
        print("Access Token: {at}".format(at = self.accessToken))

class Activity:
    def __init__(self, id, file_path = None):
        self.file_path = file_path
        if 'gpx' in self.file_path: # TODO: add case where activity source is not a file but from REST 
            self.points_original = gpx_to_lat_lon_list(self.file_path)
            self.id = id
            
            # remove points that are not within PSP bounds
            self.points_bounded = fit_points_to_bounds(self.points_original)

class Efforts: 
    def __init__(self, activities_path = None):
        self._root = activities_path
        self.activity = {}
        if activities_path != None:
            self.get_activity_points()
        
        # creds = pd.read_csv("data/credentials/credentials_sarah.csv")
        # #will be assigned for each user of the app. Will need to make switch conditionals. 
        # ATHLETE_ID = "57961903"#creds['athlete_id'][0]
        # CLIENT_ID = "76267"#creds['client_id'][0]
        # CLIENT_SECRET = "b57ab8be784c3c66b1a2551a7da2e07c5401bc8f"#creds['client_secret'][0] #'44c148263feb4f7855dd419f2af58b73df08efd0'
        # REFRESH_TOKEN = "9418628aa771a4d44b5588b42220081d61a89e47"#creds['refresh_token'][0] #'ac7791e211ecbd381f5740eb738b095351260ecf' #scope is activity:read_all
        # testing the above code in a different way
        creds = pd.read_csv("data/credentials/credentials_sarah.csv")
        CLIENT_ID = 56934#int(float(creds["client_id"].reset_index(drop = True)[0]))
        CLIENT_SECRET = '44c148263feb4f7855dd419f2af58b73df08efd0'#creds["client_secret"].reset_index(drop = True)[0]
        REFRESH_TOKEN = '1ef41c351c98df2cc88eaf31913e4bb4580872e4'#creds["refresh_token"].reset_index(drop = True)[0]
        ATHLETE_ID = 57961903#int(float(creds["athlete_id"].reset_index(drop = True)[0]))
        
        print(type(CLIENT_ID), CLIENT_ID)
        print(type(CLIENT_SECRET),CLIENT_SECRET)
        print(type(REFRESH_TOKEN), REFRESH_TOKEN)
        print(type(ATHLETE_ID), ATHLETE_ID)
        
        self.user = Athlete(clientId=CLIENT_ID, clientSecret=CLIENT_SECRET, refreshToken=REFRESH_TOKEN, athleteId=ATHLETE_ID)
        self.user.retrieveAuthToken()
        
        
    def get_activity_points(self):
        data_folder = self._root
        
        activities_lon_lat = []
        ids = []
        
        self.points_combined = np.array([0,0])
        #opens all files in the directory according to query and stores in dictionary
        for root, dirs, files in os.walk(data_folder):
            for file in files:
                if "activities" in root: # skips past the test folder in directory
                    activity_name = str.split(file, '.')[0]
                    activity = Activity(id = activity_name, file_path = root + '/' + file)
                    ids.append(activity.id) # for easy decoding by index in the future
                    activities_lon_lat.append(activity.points_bounded)
                    
                    self.points_combined = np.vstack([self.points_combined, activity.points_bounded])
                        
                    # assign Trail object to self.activity for future use
                    self.activity[activity.id] = activity
                else:
                    continue
                
        self.activity_names = ids
        self.points_by_id = activities_lon_lat
        self.points_combined = self.points_combined[1:, :]
    
    def get_activities_from_strava(self):
        BASE_URL = 'https://www.strava.com/api/v3/'

        headers2 = {"Authorization": "Bearer {token}".format(token = self.user.accessToken)}
        print(headers2)
        startYear = 2020
        startMonth = 5
        startDay = 1
        d_start = datetime.datetime(startYear, startMonth, startDay, 0, 0) # 0 , 0 - (h, m)
        
        
        afterDate = calendar.timegm(d_start.timetuple())
        
        today = datetime.datetime.today()
        
        beforeDate = calendar.timegm(today.timetuple())
        params2 = {'per_page': 500, 'page':1, 'after':afterDate, 'before':beforeDate}
        # params2 = {'after':afterDate}
        url2 = BASE_URL + "athlete/activities"
        response = requests.get(url2, params = params2, headers = headers2)
        print("Response2: {code}".format(code = response))
        response_json = response.json()

        self.activities_list_json = response_json
        #parse activities into activity list
        self.activityIdList = []
        self.sufferScoreList = []
        for index in range(len(response_json)):
            activityId = response_json[index]['id']
            self.activityIdList.append(activityId)
            #print(activityId)
            sufferScore = response_json[index]['suffer_score']
            self.sufferScoreList.append(sufferScore)
            

        print("Activities found: {count}".format(count = len(self.activityIdList)))
        
        self.lonlatList = []
        #extend the lat long data from each activity into self.lonlatList
        #add total distance to a counter 
        self.totalDistanceTraveled = 0
        self.lonlatPerActivity = {}
        self.totalElevationGained = 0
        
        for activity in self.activityIdList:
            headers3 = {"Authorization": "Bearer {token}".format(token = self.user.accessToken)}
            params3 = {"id": activity, "keys": "latlng,altitude", "key_by_type":"true"}
            url3 = BASE_URL + "activities/{activityId}/streams".format(activityId = activity)
            url5 = BASE_URL + "activities/{activityId}".format(activityId = activity)
            response3 = requests.get(url3, params = params3, headers = headers3)
            response5 = requests.get(url5, headers = headers3)
            print("Response3: {code}".format(code = response3))
            data5 = response5.json()["total_elevation_gain"]
            #print(data5)
            self.totalElevationGained = self.totalElevationGained + data5
            
            response3_json = response3.json()
            
            if (not ("latlng" in response3_json.keys())): # for activities without lat long info such as workouts
                continue
                
            lonlatData = response3_json["latlng"]["data"]
            
            self.lonlatPerActivity[activity] = lonlatData
            self.lonlatList.extend(lonlatData)
            #print("Lat Lon List: {list}".format(list = self.lonlatList))

            distanceList = response3_json["distance"]["data"]
            distance = distanceList[len(distanceList) - 1]
            self.totalDistanceTraveled = self.totalDistanceTraveled + distance 
        # for compatability with already written code, switch lonlatList[0] and lonlatList[1] (which makes first column longitude) 
        
        print(len(self.lonlatList))
        
        if len(self.lonlatList) > 0:
            lat0lon1 = np.array(self.lonlatList)
            
            print(lat0lon1.shape)

            swapped = np.zeros((len(lat0lon1), 2))
            swapped[:, 0] = lat0lon1[:, 1]
            swapped[:, 1] = lat0lon1[:, 0]
            
            self.lonlatList = swapped
            self.lonlatList = fit_points_to_bounds(self.lonlatList)
            
            print("Total Distance: {dist}".format(dist = self.totalDistanceTraveled))

        else:
            print("No activities with distance found.")
            exit()
            

    
        

class Trail:
    def __init__(self, file_path, id):
        self.file_path = file_path
        self.id = id
        self.points_list = gpx_to_lat_lon_list(self.file_path)
        self.points_array = np.array(self.points_list)
        self.completed = False
    
    def compare_to(self, points):
        per_complt = match_maps(points, self.points_list)
        if per_complt > 0.96:
            self.completed = True
            print("{t} Trail Completed".format(t = self.id))
        else:
            print("{t} Trail is {p} Covered".format(t = self.id, p = per_complt))
        
class Park:
    def __init__(self, trails_path):
        self._root = trails_path
        self.trail = {}
        self.get_trail_points()
        
    def get_trail_points(self):
        data_folder = self._root
        # contains lon, lat of each file in a separate index 
        trails_lon_lat = []
        trail_names_by_idx = []
        self.points_combined = np.array([0,0])
        #opens all files in the directory according to query and stores in dictionary
        for root, dirs, files in os.walk(data_folder):
            for file in files:
                if "trails" in root: # skips past the test folder in directory
                    trail_name = str.split(file, '.')[0]
                    trail = Trail(root + '/' + file, trail_name )
                    trail_names_by_idx.append(trail.id) # for easy decoding by index in the future
                    
                   
                    self.points_combined = np.vstack([self.points_combined, trail.points_array])
                        
                    trails_lon_lat.append(trail.points_list)
                    
                    
                    # assign Trail object to self.trail for future use
                    self.trail[trail.id] = trail
                    
                else:
                    continue
        
        self.points_combined = self.points_combined[1:, :]
        self.trail_names = trail_names_by_idx
        self.points_by_id = trails_lon_lat
        
    
        