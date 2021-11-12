#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/pablobottero/github/master/python/data_analysis')


bikes2011 = pd.read_csv('rentals_weather_2011.csv')
del rentals_weather_2011['index2']
del rentals_weather_2011['dteday_y']
bikes2011 = bikes2011.rename(columns={'dteday_x':'dteday'})
bikes2012 = pd.read_csv('rentals_weather_2012.csv', sep=';', decimal=',')
bikes11_12 = bikes2011.append(bikes2012, ignore_index=True)

rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True)
wbr=rentals_weather_11_12

mytable = wbr.groupby(['weathersit']).size()

print(mytable)

mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)


#Barchart1
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2)
