# Testing for activity class
from gpxpy import gpx
from global_functions import gpx_to_lat_lon_list, fit_points_to_bounds, match_maps
import os
import numpy as np 

class Activity:
    def __init__(self, id, file_path = None):
        self.file_path = file_path
        if 'gpx' in self.file_path: # TODO: add case where activity source is not a file but from REST 
            self.points_original = gpx_to_lat_lon_list(self.file_path)
            self.id = id
            
            # remove points that are not within PSP bounds
            self.points_bounded = fit_points_to_bounds(self.points_original)

class Efforts: 
    def __init__(self, activities_path):
        self._root = activities_path
        self.activity = {}
        self.get_activity_points()
        
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
        
    
        