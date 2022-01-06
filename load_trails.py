# Purpose of this is to import all the trail gpx files and get them in a usable format
#%%
from global_functions import gpx_to_lat_lon_list, label_lat_lons, calculate_distances, fit_points_to_bounds
import os
import matplotlib.pyplot as plt
from itertools import cycle 
import numpy as np

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

# # plot the trails
# colors = cycle(['red', 'orange','yellow','green','blue','purple'])

# for trail, color in zip(range(len(labelled_pts)), colors):
#     x_points = labelled_pts[labelled_pts[:, 2] == trail][:, 0]
#     y_points = labelled_pts[labelled_pts[:, 2] == trail][:, 1]
    
#     plt.scatter(x = x_points, y = y_points, c = color)

# plt.show()

