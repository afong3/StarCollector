# very informal tests 
#%%
from global_functions import gpx_to_lat_lon_list, label_lat_lons, calculate_distances, fit_points_to_bounds
import matplotlib.pyplot as plt
import global_functions
import numpy as np
import pandas as pd
import scipy.spatial
import os
import classes
import warnings 
warnings.filterwarnings('ignore')
import gpxpy

# SAMPLE
# summary of what it is, when it passes, etc. 
def test_X():
    print("------- START TEST X -------")

    # fun test stuff    
    pass

    print("------- END TEST X -------")


# fit_points_to_bounds
## ex: fits the activity https://www.strava.com/activities/4778236056 to psp 
## Visually passes if the bits that are in pacific spirit are kept but the ones outside are not 
def test_0():
    print("------- START TEST 1 -------")

    test_bb = gpx_to_lat_lon_list('data/tests/test_bounds.gpx')
    bounded = fit_points_to_bounds(test_bb)

    print("Bounded: {b}, OG: {og}".format(b = len(bounded), og = len(test_bb)))

    plt.scatter(x = np.array(test_bb)[:, 0], y = np.array(test_bb)[:, 1], c = "red", label = "Original", alpha = 0.2, s = 30)
    plt.scatter(x = bounded[:, 0], y = bounded[:, 1], c = "blue", label = "Bounded", alpha = 0.2, s = 12)
    plt.legend()

    plt.show()
    
    print("------- END TEST 0 -------")

# test of the logic that calculates percentage of a trail completed based on an activity 
# Visually passes if the portion of the trail that was not traced by the activity is highlighted
def test_1():
    print("------- START TEST 1 -------")

    # comparing a run that I just did and how much of spanish trail that I've completed as an example of how to use this information
    files = ["data/tests/test_run.gpx", "data/tests/test_spanish_trail.gpx"]

    lat_lon_list = []
    for file in files:
        gpx = gpx_to_lat_lon_list(file)
        lat_lon_list.append(gpx)
        
    labelled_pts = label_lat_lons(lat_lon_list)
        
    tolerance = 0.00015 # this is from trial and error to get the right amount of overlapping data points
    tree = scipy.spatial.KDTree(labelled_pts[:, :2])
    points_within_tolerance = tree.query_ball_point(labelled_pts[:, :2], tolerance)


    vfunc = np.vectorize(lambda a: np.any(labelled_pts[a, 2] != labelled_pts[a[0], 2]))

    matches = vfunc(points_within_tolerance)
    matching_points = labelled_pts[matches, :2]

    df = pd.DataFrame(labelled_pts)
    mp = pd.DataFrame(matching_points)
    st = pd.DataFrame(df[df[2] == 1.0][[0,1]])

    diff_df = pd.merge(mp,st, how = "inner", on = [0,1])
    plt.scatter(x = st[0], y = st[1], c = "r", alpha = 0.6, label = "Spanish Trail")
    #plt.scatter(x = df[0], y = df[1], c = df[2], alpha = 0.2)
    plt.scatter(x = diff_df[0], y = diff_df[1], c = "silver", label = "Portion of Trail Ran")
    # for clust_idx in set(clusters):
    #     plt.scatter(matching_points[clusters == clust_idx,0], matching_points[clusters == clust_idx,1], c = "pink", s = 50, alpha = 0.6)
    plt.xticks(rotation = 30)
    plt.ylabel("Latitude")
    plt.xlabel("Longitude")
    plt.title("Overlap of A Run and Spanish Trail")
    plt.legend()
    plt.show()
    
    plt.scatter(x = df[df[2] == 0.0][0], y = df[df[2] == 0.0][1], c = "blue", label = "GPX Track of Activity")
    plt.scatter(x = st[0], y = st[1], c = "r", alpha = 0.6, label = "Spanish Trail")

    plt.xticks(rotation = 30)
    plt.ylabel("Latitude")
    plt.xlabel("Longitude")
    plt.title("Simple Plot of A GPX Recording")
    plt.legend()
    plt.show()
        
    test_dist = calculate_distances(df[df[2] == 0.0][[0,1]])
    st_dist = calculate_distances(st)
    diff_dist = calculate_distances(diff_df)

    print("Percent of Spanish Trail Completed: {0}".format(diff_dist / st_dist))# %%

    print("------- END TEST 1 -------")


#Tests loading all the trails and making sure that they are in the right location, etc. 
# Visually passes if the trails resemble the trails you want them to 
def test_2():
    print("------- START TEST 2 -------")

    data_folder = "data"
    # contains lon, lat of each file in a separate index 
    trails_lat_lons = []
    trail_names_by_id = []
    #opens all files in the directory according to query and stores in dictionary
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if "trails" in root: # skips past the test folder in directory
                trail_name = str.split(file, '.')[0]
                trail_names_by_id.append(trail_name) # for easy decoding by index in the future
                trails_lat_lons.append(gpx_to_lat_lon_list(root + '/' + file))
            else:
                continue
            
    # create unique int id for each trail 
    labelled_pts = label_lat_lons(trails_lat_lons)

    # # plot the trails (TAKES A MINUTE OR SO, UNCOMMENT WHEN NECESSARY)
    # colors = cycle(['red', 'orange','yellow','green','blue','purple'])

    # for trail, color in zip(range(len(labelled_pts)), colors):
    #     x_points = labelled_pts[labelled_pts[:, 2] == trail][:, 0]
    #     y_points = labelled_pts[labelled_pts[:, 2] == trail][:, 1]
        
    #     plt.scatter(x = x_points, y = y_points, c = color)

    # plt.show()

    print("------- END TEST 2 -------")

# Tests if all activites can be loaded from a path
# Passes if no error is thrown
def test_3():
    print("------- START TEST 3 -------")
    data_folder = "data/"
    activities = []
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if "activities" in root: # skips past the test folder in directory
                activity_name = str.split(file, '.')[0]
                path = root + '/' + file
                #print(path)
                activities.append(classes.Activity(activity_name, file_path = path))
            else:
                continue
    

    print("------- END TEST 3 -------")

# Verify that each gpx file only contains trails which match the filename
# 
def test_4():
    print("------- START TEST 4 -------")
    data_folder = "data/"
    activities = []
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if "trails" in root: # skips past the test folder in directory
                trail_name = str.split(file, '.')[0]
                path = root + '/' + file
                gpx_file = open(path, "r", encoding = "utf8")
                gpx = gpxpy.parse(gpx_file)                
                
                track_counter = 0
                for track in gpx.tracks:
                    if trail_name in track.name:
                        track_counter += 1
                        continue
                    else:
                        track_counter += 1
                        print("{t} Has Incorrect Trails".format(t = trail_name))
                        
                print("{t} Count: {c}".format(t = trail_name, c = track_counter))
                
            else:
                continue
    

    print("------- END TEST 4 -------")

# Completes a relatively quick map matching and finds the progress on every trail
def test_5():
    print("------- START TEST 5 -------")

    trails_path = "data/trails"
    P = classes.Park("data/trails")

    activities_path = "data/activities"
    E = classes.Efforts(activities_path)

    #P.trail["Admiralty"].compare_to(E.points_combined)

    # for trail in P.trail_names:
    #     P.trail[trail].compare_to(E.points_combined)
    
    df = global_functions.match_maps(E.points_combined, P.points_by_id)
    
    for i in range(1, 43, 1):
        print(len(P.trail_names))
        trail_name = P.trail_names[i - 1] # -1 bedcause the df's trail count will be incremented length of total trails
        trail = P.trail[trail_name]
        trail_point_count = len(trail.points_list)
        trail_match_count = len(df[df[2] == i])
        trail.matched_points = df[df[2] == i][[0,1]]
        
        plt.scatter(x = trail.points_array[:, 0], y = trail.points_array[:, 1], c = "red", s = 15, label = "{trail} Trail".format(trail = trail_name))
        #plt.scatter(x = df[df[2] == i][0], y = df[df[2] == i][1], c = "blue", label = "Matched Points", marker = ',', s = 2)
        plt.scatter(x = P.trail[trail_name].matched_points[0], y = P.trail[trail_name].matched_points[1], c = "blue", label = "Matched Points", marker = ',', s = 2)
        plt.legend()
        plt.show()
        print("{trail} is {p} complete".format(trail = trail_name, p = trail_match_count / trail_point_count))

        

    print("------- END TEST 5 -------")

# Creates a map from activities in a filepath.  
def test_6():
    print("------- START TEST 6 -------")
    trails_path = "data/trails"
    P = classes.Park("data/trails")

    activities_path = "data/activities"
    E = classes.Efforts(activities_path)
    
    df = global_functions.match_maps(E.points_combined, P.points_by_id)
    
    points_total = 0 
    points_total_matched = 0
    
    for i in range(1, len(P.trail_names) + 1, 1):
        trail_name = P.trail_names[i - 1] # -1 bedcause the df's trail count will be incremented length of total trails
        trail = P.trail[trail_name]
        trail_point_count = len(trail.points_list)
        trail_match_count = len(df[df[2] == i])
        P.trail[trail_name].points_matched = df[df[2] == i][[0,1]]
        
        points_total += trail_point_count
        points_total_matched += trail_match_count
        
        
    print("{prog} of {total} Achieved".format(prog = points_total_matched, total = points_total))
    global_functions.create_map(P)

    print("------- END TEST 6 -------")

# Ok, this test creates a map for the hardcoded athlete_id, refresh_token, etc. 
def test_7():
    print("------- START TEST 7 -------")
    # Retrieves access token for activity:read_all scope
    trails_path = "data/trails"
    P = classes.Park("data/trails")
    E = classes.Efforts()
    
    E.get_activities_from_strava()
    
    df = global_functions.match_maps(E.lonlatList, P.points_by_id)
        
    points_total = 0 
    points_total_matched = 0

    for i in range(1, len(P.trail_names) + 1, 1):
        trail_name = P.trail_names[i - 1] # -1 bedcause the df's trail count will be incremented length of total trails
        trail = P.trail[trail_name]
        trail_point_count = len(trail.points_list)
        trail_match_count = len(df[df[2] == i])
        P.trail[trail_name].points_matched = df[df[2] == i][[0,1]]
        
        points_total += trail_point_count
        points_total_matched += trail_match_count
        
        
    print("{prog} of {total} Achieved".format(prog = points_total_matched, total = points_total))
    global_functions.create_map(P)
    

    print("------- END TEST 7 -------")

# Have user log into strava, authorize the app, and take the refresh_token and athlete id
def test_8():
    print("------- START TEST 8 -------")

    from urllib import request
    import webbrowser
    import requests
    import os
    from oauthlib.oauth2 import WebApplicationClient

    client_id = 56934
    client = WebApplicationClient(client_id)

    authorization_url = "https://www.strava.com/oauth/authorize"

    url = client.prepare_request_uri(
    authorization_url,
    redirect_uri = 'https://localhost',
    scope = ['activity:read_all'],
    state = 'D8VAo311AAl_49LAtM51HA'
    )
    
    print(url)
    
    
    # url = "https://www.strava.com/oauth/authorize?client_id=56934&redirect_uri=http%3A%2F%2Flocalhost&response_type=code&approval_prompt=auto&scope=activity:read_all#"
    # response = webbrowser.open(url)
    # print(response)
    # response1 = request.urlopen(url)    
    # print(response1.status)
    # strava_login_url = response1.geturl()
    # print(strava_login_url)
    
    # response2 = request.urlopen(strava_login_url)
    # webbrowser.open(strava_login_url)
    # print(response2.status)
    # print(response2.geturl())
    
# Automatically opens the map made in a webbrowser
def test_9():
    print("------- START TEST 9 -------")
    import webbrowser

    map_path = "c:/code/python/mapMatcher/data/maps/map_01-07-2022.html"
    
    url = 'file://{}'.format((map_path))
    print(url)
    webbrowser.open(url,2)
    

    print("------- END TEST 9 -------")

if __name__ == "__main__":
    test_7()
    
# %%
