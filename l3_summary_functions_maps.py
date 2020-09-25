# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 22:33:37 2020

@author: user
"""


# mainly taken from here:
# https://www.kaggle.com/learn/pandas

import pandas as pd
import os

# load from file
folder = 'datasets'
file = 'winemag-data-130k-v2.csv'

# wine_reviews = pd.read_csv( os.path.join( folder , file ) )
# the file already includes and index column that pandas ignore and construct its own
# to force pandas use the firts column already in the file as index, do the following:
wine_reviews = pd.read_csv( os.path.join( folder , file ) , index_col=0 )

# summary functions
points_summary = wine_reviews.points.describe()
points_mean = wine_reviews.points.mean()

tester_name_summary = wine_reviews.taster_name.describe()
tester_name_unique = wine_reviews.taster_name.unique()
tester_name_value_counts = wine_reviews.taster_name.value_counts()

# maps
points_centralized = wine_reviews.points.map( lambda p : p - points_mean )

# apply
def centralise_points(row):
    row.points = row.points - points_mean
    return row

points_centralized_0 = wine_reviews.apply( centralise_points , axis='columns' )

region = wine_reviews.country + '-' + wine_reviews.region_1
