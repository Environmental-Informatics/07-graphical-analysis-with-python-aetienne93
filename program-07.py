#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:52:38 2020
this script reads in a USGS earthquake CSV file containing all measureable earthquakes in USGS database from the past 30 days.
Analysis is performed on the data including, histogram of magnitudes, KDE plot of density v. magnitude, cum dist. of earthquake depth,
scatterplot with depth v. magnitude, and QQ-plot with normally distributed magnitudes 
@author: aetienne
@github: aetienne93
"""
"""load in necessary packages""" 
import numpy as np
import pandas
from scipy import stats
import pylab
import matplotlib.pyplot as plt
import seaborn as sns

"""read in data from USGS all-earthquake 
    comma seperated"""
all_quake = pandas.read_table('all_month.csv',sep="," )


""" creates a histogram for magnitudes of all earthquakes in 'all_quake'"""

N, bins, patches = plt.hist(all_quake['mag'], bins=10, range=(0,10),color='black')
for i in range (0,1):
    patches[i].set_facecolor('b')
for i in range (1,2):
    patches[i].set_facecolor('g')
for i in range (2,3):
    patches[i].set_facecolor('r')
for i in range (3,4):
    patches[i].set_facecolor('m')
for i in range (4,5):
    patches[i].set_facecolor('y') 
for i in range (5,6):
    patches[i].set_facecolor('k')
plt.title("Earthquake frequency vs. magnitude")
plt.xlabel("Magnitude", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()


"""doesn't function correctly
pandas.quake=all_quake['mag']
pandas.quake.plot.kde(bw_method=0.3)
plt.xlabel('Magnitude', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.show()
"""

"""creates KDE plot with gaussian kernel, width set to 0.3"""
sns.kdeplot(np.array(all_quake['mag']),kernel='gau',bw=0.3)
plt.title("Earthquake density vs. magnitude")
plt.xlabel('Magnitude', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.show()

"""creates a plot of all quakes, based on longitude and latitiude, plotted on 
x and y axes respectively""" 

plt.plot(all_quake["longitude"], all_quake["latitude"], 'g^', label='Mean')
plt.title("Earthquake occurence map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()


"""creates a normal cumulative distribution plot of earthquake depths- in kilometers"""
plt.hist(all_quake['depth'], bins=400, cumulative=True,color='red')
plt.title("Normal cumulative distribution of earthquake depths")
plt.xlabel("Depth (Km)")
plt.ylabel("Cumulative Frequency")
plt.show()

"""creates a scatterplot of earthquake magnitude vs. depth, plotted on x and y 
axes respecitvely"""
plt.scatter(all_quake['mag'], all_quake['depth'], c='m',marker='.')
plt.title("Earthquake Magnitude vs. Depth")
plt.xlabel("Magnitude")
plt.ylabel("Depth (Km)")
plt.show()

"""creates a Q-Q plot of all earthquate magnitudes- assume normal distribution 
of values"""
stats.probplot(all_quake['mag'], dist='norm',plot=pylab)
#stats.set_title("Normally Distributed Earthquake Magnitudes")
plt.show()