# Testing map matching with KDTree algorithm
#%%

# purpose is to show a proof of concept example to create the bulk of the calculations off of 
# some inspiration goes to https://gis.stackexchange.com/questions/81551/matching-gps-tracks
# GPX tracks for all (or most?) trails tediously made on caltopo.com (but it was fun, I listened to two albums. 2 hours!)

from numpy.matrixlib.defmatrix import mat
import scipy.spatial
import pandas as pd
import numpy as np 
import gpxpy
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import warnings 

warnings.filterwarnings('ignore')

def gpx_to_lat_lon_list(filename):
    """
    Summary: takes a .gpx file and turns the latitude and longitudes into a list of tuples
    
    Returns: list of tuples (latitude, longitude).
    """
    gpx_file = open(filename, "r")
    gpx = gpxpy.parse(gpx_file)
    
    latlonlist = []
    if len(gpx.tracks) > 0:
        print("tracks")
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    latlonlist.append((point.longitude, point.latitude))
    elif len(gpx.routes) > 0:
        print("routes")
        for route in gpx.routes:
            for point in route.points:
                latlonlist.append((point.longitude, point.latitude))
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

if __name__ == "__main__":
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
