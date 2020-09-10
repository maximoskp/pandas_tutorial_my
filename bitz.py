# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:37:34 2020

@author: maximos
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import scipy.stats as spst

results = pd.read_csv( os.path.join( 'datasets' , 'bitzounis_results.csv' ) , decimal='.' )

stages = ['circuit', 'carmona', 'sprint', 'laguna']

for s in stages:
    # max
    fast_max = results[ s + '_' + 'fast_max']
    fast_max = fast_max[ ~pd.isna(fast_max) ]
    
    slow_max = results[ s + '_' + 'slow_max']
    slow_max = slow_max[ ~pd.isna(slow_max) ]
    
    w_max = spst.wilcoxon( fast_max , slow_max )[1]
    
    plt.clf()
    plt.boxplot( [slow_max, fast_max] ); plt.title(str( w_max ))
    plt.savefig(os.path.join('figs_bitz',  s + '_' + 'max.png'), dpi=300)
    
    # avg
    fast_avg = results[ s + '_' + 'fast_avg']
    fast_avg = fast_avg[ ~pd.isna(fast_avg) ]
    
    slow_avg = results[ s + '_' + 'slow_avg']
    slow_avg = slow_avg[ ~pd.isna(slow_avg) ]
    
    w_avg = spst.wilcoxon( fast_avg , slow_avg )[1]
    
    plt.clf()
    plt.boxplot( [slow_avg, fast_avg] ); plt.title(str( w_avg ))
    plt.savefig(os.path.join('figs_bitz',  s + '_' + 'avg.png'), dpi=300)
    
    # time
    fast_time = results[ s + '_' + 'fast_time']
    fast_time = fast_time[ ~pd.isna(fast_time) ]
    
    slow_time = results[ s + '_' + 'slow_time']
    slow_time = slow_time[ ~pd.isna(slow_time) ]
    
    w_time = spst.wilcoxon( fast_time , slow_time )[1]
    
    plt.clf()
    plt.boxplot( [slow_time, fast_time] ); plt.title(str( w_time ))
    plt.savefig(os.path.join( 'figs_bitz', s + '_' + 'time.png'), dpi=300)