# Serves as a functional module
import gpxpy
import numpy as np
import pandas as pd
import geopandas as gpd
import scipy.spatial
import matplotlib.pyplot as plt
import datetime
import folium
import random
import time
from shapely.geometry.linestring import LineString

# TODO: Change hardcoded bounds to be derived from all the trail gpx files 
BB_LAT = [49.225, 49.285]
BB_LON = [-123.275, -123.19]

def gpx_to_lat_lon_list(filename):
    """
    Summary: takes a .gpx file and turns the longitude and latitude into a list of tuples
    
    Returns: list of tuples (longitude, latitude).
    """
    gpx_file = open(filename, "r", encoding = "utf8")
    gpx = gpxpy.parse(gpx_file)
    
    latlonlist = []
    if len(gpx.tracks) > 0:
        #print("tracks")
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    latlonlist.append([point.longitude, point.latitude]) # CHANGED THESE FROM TUPLES TO LISTS LETS SEE IF THIS DOES ANYTHING
    elif len(gpx.routes) > 0:
        #print("routes")
        for route in gpx.routes:
            for point in route.points:
                latlonlist.append([point.longitude, point.latitude])
    else:
        print("sorry mate, didn't care enough to implement this")
    return latlonlist

def label_lat_lons(lats_and_longs: list):
    """
    Summary: Labels the lats and longs so that each gpx file has a unique integer id
    
    :param lats_and_longs: A List of all latlonlists
    
    Returns: np.ndarray with each row being its own np.array of np.array([latitude, longitude, gpx_file_id])
    """
    df_list = []
    for idx, l in enumerate(lats_and_longs):
        df = pd.DataFrame(l)
        df.columns = ["longitude", "latitude"]
        df["id"] = idx
        
        df_list.append(df)
    
    nd_arr = np.array([[0,0,0]])
    for df in df_list:
        nd_arr = np.vstack([nd_arr, df.to_numpy()])
        
    return nd_arr[1:, :]

#IN PROGRESS
def match_maps(gpx1, gpx2):
    """
    How many points from gpx1 cross gpx2?
    
    Returns: the points
    """
    if type(gpx2) == list:
        lat_lon_list = gpx2
        lat_lon_list.insert(0, gpx1)
    else:
        lat_lon_list = [gpx1, gpx2]

    labelled_pts = label_lat_lons(lat_lon_list)
        
    tolerance = 0.00015 # this is from trial and error to get the right amount of overlapping data points
    tree = scipy.spatial.KDTree(labelled_pts[:, :2])
    points_within_tolerance = tree.query_ball_point(labelled_pts[:, :2], tolerance)

    vfunc = np.vectorize(lambda a: np.any(labelled_pts[a, 2] != labelled_pts[a[0], 2]))

    matches = vfunc(points_within_tolerance)
    matching_points = labelled_pts[matches, :2]

    mp = pd.DataFrame(matching_points)
    trail = pd.DataFrame(labelled_pts)

    diff_df = pd.merge(mp,trail, how = "inner", on = [0,1])
    # plt.scatter(x = trail[0], y = trail[1], c = "r", alpha = 0.6, label = "Trail")
    # #plt.scatter(x = df[0], y = df[1], c = df[2], alpha = 0.2)
    # plt.scatter(x = diff_df[0], y = diff_df[1], c = "silver", label = "Portion of Trail Ran")
    # # for clust_idx in set(clusters):
    # #     plt.scatter(matching_points[clusters == clust_idx,0], matching_points[clusters == clust_idx,1], c = "pink", s = 50, alpha = 0.6)
    # plt.xticks(rotation = 30)
    # plt.ylabel("Latitude")
    # plt.xlabel("Longitude")
    # plt.title("Overlap of A Run and Trail")
    # plt.legend()
    # plt.show()
    
    # plt.scatter(x = df[df[2] == 0.0][0], y = df[df[2] == 0.0][1], c = "blue", label = "GPX Track of Activity")
    # plt.scatter(x = trail[0], y = trail[1], c = "r", alpha = 0.6, label = "Trail")

    # plt.xticks(rotation = 30)
    # plt.ylabel("Latitude")
    # plt.xlabel("Longitude")
    # plt.title("Simple Plot of A GPX Recording")
    # plt.legend()
    # plt.show()
        
    # test_dist = calculate_distances(df[df[2] == 0.0][[0,1]])
    trail_dist = calculate_distances(trail.copy())
    diff_dist = calculate_distances(diff_df.copy())

    #print("Percent of Trail Completed: {0}".format(diff_dist / trail_dist))# %%
    return diff_df
    
def calculate_distances(points_df: pd.DataFrame):
    """
    Summary: Calculates the total distance in a pd.DataFrame of lon / lat points (Must be arranged in this order).
    Best used to calculate the percentage of a trail completed. For example, divide the distance of 
    the difference between a inner merge between the matched points and the points from the true trail gpx
    to find the percentage of that trail you have completed. 
    
    :parameter points_df: A pd.DataFrame that has the first column as longitude and the second column as latitude.
    
    Returns: float value of total distance in dataframe
    """
    gdf = gpd.GeoDataFrame(points_df, geometry = gpd.points_from_xy(points_df[0], points_df[1]))
    gdf["prev_geom"] = gdf.shift()["geometry"]
    
    # drop rows with None
    gdf = gdf.dropna().reset_index()
    gdf["distance"] = gpd.GeoSeries.distance(gdf["prev_geom"], gdf["geometry"])
    gdf["distance"][gdf["distance"] > 0.003] = 0 # accounting for values that have big gaps between recording(100 m) 
    dist_sum = gpd.GeoSeries.sum(gdf["distance"])
    return(dist_sum)

def fit_points_to_bounds(points, BB_lon0 = BB_LON[0], BB_lat0 = BB_LAT[0], BB_lon1 = BB_LON[1], BB_lat1 = BB_LAT[1]): 
    """
    Summary: Bound all lon/lats to a bounding box (BB_LON, BB_LAT). 0 is min and 1 is max bound. Defaults are PSP bounds.
    Returns: np.array of points in the park. 
    """
    
    # column 0 is longitude, column 1 is latitude
    id = np.nan
    if type(points) == list:
        points = np.array(points)
    elif type(points) == np.array:
        # get rid of id if id is present
        if(points.shape[1] > 2): 
            id = points[:, 2]
            points = points[:, :2]
            
    lon_cond_0 = points[:, 0] > BB_LON[0]
    lon_cond_1 = points[:, 0] < BB_LON[1]
    
    lat_cond_0 = points[:, 1] > BB_LAT[0]
    lat_cond_1 = points[:, 1] < BB_LAT[1]
    
    lon_cond = np.logical_and(lon_cond_0, lon_cond_1)
    lat_cond = np.logical_and(lat_cond_0, lat_cond_1)
    
    condition = np.logical_and(lon_cond, lat_cond)
    
    psp_points = points[condition]
    
    return psp_points

    if id != np.nan: # TODO: add this just in case the points have an id
        # there was an id on the input np.array
        pass

def randomHexColor():
    ts = datetime.datetime.now().timestamp()
    additionalWeight = int((ts % 2)*333)
    changingValue = int(ts) + additionalWeight
    random.seed(changingValue)
    #creating random color 
    hexArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9','a','b','c','d','e','f']
    hexVals = {}
    randomColor = '#'
    for index in range(6):
        hexVals[index] = random.choice(hexArray)
        randomColor = randomColor + hexVals[index]

    time.sleep(0.1)
    #print(randomColor)
    return(randomColor)

# IN PROGRESS
# TODO: There's a problem with how this is plotting. Because the items are LineStrings and not Markers, the points have the issue that Strava has. 
# When there's a large gap in distance between gpx points, they still draw a stright line between them. This leaves an illegible graph. 
# I need to somehow account for leaving the gaps unlined. Maybe this has to be a fundamental change as well. Maybe the graph could show
# a different color for a different Trail.state. Such as, completed = True, trails can be green and completed = False trails can be red. 

def create_map(P):
    crs = {'init': 'epsg:4326'}
    startingLocation = [BB_LON[0], BB_LAT[0]]
    # print(self.lonPerActivity)
    # print(self.latPerActivity)
    zoom = 1
    trail_lines = {}
    progress_lines = {}
    m = folium.Map(startingLocation, zoom_start = zoom, tiles = "cartodbpositron")

    # add iterative folium items to the map obect
    for trail_name in P.trail_names:
                
        trail = P.trail[trail_name]
        trail_lons = trail.points_array[:, 0]
        trail_lats = trail.points_array[:, 1]
        progress_lons = trail.points_matched[0]
        progress_lats = trail.points_matched[1]
        
        plt.scatter(x = progress_lons, y = progress_lats, c = "pink")
        plt.show()
        
        line_geom_trail = LineString(zip(trail_lons, trail_lats))
        line_geom_progress = LineString(zip(progress_lons, progress_lats))
        
        trail_lines[trail_name] = gpd.GeoDataFrame(index = [0], crs = crs, geometry = [line_geom_trail])
        progress_lines[trail_name] = gpd.GeoDataFrame(index = [0],crs = crs, geometry = [line_geom_progress])
        
        #randomCol = randomHexColor()
        #style = {'color': "blue"} 
        
        #folium.GeoJson(trail_lines[trail_name], style_function = lambda x:style, control = False, name = trail_name).add_to(m)
        
        #randomCol = randomHexColor()
        style = {'color': "red"} 
        
        folium.GeoJson(progress_lines[trail_name], style_function = lambda x:style, control = True, name = trail_name + " Progress").add_to(m)
        
        folium.LatLngPopup().add_to(m)

    # add non iterative folium items to the map object 
    folium.TileLayer("Stamen Terrain").add_to(m)
    folium.TileLayer("Open Street Map").add_to(m)
    
    folium.LayerControl().add_to(m)

    currentDate = datetime.date.today().strftime("%m-%d-%Y")
    
    m.save("map_{date}.html".format(date = currentDate))
