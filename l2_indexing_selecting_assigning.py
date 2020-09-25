# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:19:06 2020

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
h = wine_reviews.head()

# check out the components in one column
# countries = wine_reviews.country
countries = wine_reviews['country']
# or get specific country
c = countries[0]

# index-based selection
# i01 = wine_reviews[0] # CANNOT DO
i02 = wine_reviews.iloc[0]
i03 = wine_reviews.iloc[:,3]
# i04 = wine_reviews.iloc[:,'points'] # CANNOT DO - but loc can do
i05 = wine_reviews.iloc[:3,3:]
hm1 = wine_reviews.iloc[-5:]

l01 = wine_reviews.loc[:,'points']
l02 = wine_reviews.loc[:,['points', 'taster_name']]

'''
# setting index
wine_reviews.set_index('country')
it = wine_reviews['Italy']
'''

it1 = wine_reviews.country == 'Italy' # returns true/false per index
it2 = wine_reviews.loc[ wine_reviews.country == 'Italy' ] # returns the actual data
it3 = wine_reviews.loc[ (wine_reviews.country == 'Italy') & (wine_reviews.points >= 95) ]

itfr1 = wine_reviews.loc[ wine_reviews.country.isin(['Italy', 'France']) ]

nnp = wine_reviews.loc[ wine_reviews.price.notnull() ]

# assigning
wine_reviews.loc[ wine_reviews.country == 'France' , 'country' ] = 'Frans'
# if it was like so:
# wine_reviews.loc[ wine_reviews.country == 'France' ] = 'Frans'
# the entire row would be affected

wine_reviews['index_backwards'] = range(len(wine_reviews), 0, -1)