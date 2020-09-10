# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:05:44 2020

@author: maximos
"""

# mainly taken from here:
# https://www.kaggle.com/learn/pandas

import pandas as pd
import os

# examples of generating from dictionaries
# df = pd.DataFrame( {'Yes': [12,54] , 'No': [45,32] } )
# df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
# with custom index
df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B']) # outside the dictionary

# dataframe is a table, Series is a list
# s = pd.Series([3,4,5,6])
# that can also have custom index
s = pd.Series([3,4,5,6], index=['trimester 1','trimester 2', 'trimester 3','trimester 4'])

# load from file
folder = 'datasets'
file = 'winemag-data-130k-v2.csv'

# wine_reviews = pd.read_csv( os.path.join( folder , file ) )
# the file already includes and index column that pandas ignore and construct its own
# to force pandas use the firts column already in the file as index, do the following:
wine_reviews = pd.read_csv( os.path.join( folder , file ) , index_col=0 )
# get shape
sh = wine_reviews.shape
# for quick examination, grab the first five rows with head
hd = wine_reviews.head()


import matplotlib.pyplot as plt
overall_points = wine_reviews['points']
g = wine_reviews[ wine_reviews['country'] == 'Greece' ]
gp = g['points']
it = wine_reviews[ wine_reviews['country'] == 'Italy' ]
itp = it['points']
sp = wine_reviews[ wine_reviews['country'] == 'Spain' ]
spp = sp['points']
plt.clf();plt.boxplot([overall_points, gp, itp, spp]);plt.savefig('test.png',dpi=300)
