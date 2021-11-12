#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Get working directory
os.getcwd()
os.chdir('/Users/pablobottero/github/master/python/data_analysis/second_sesion')
os.getcwd()

rentals_2011= pd.read_csv('washington_bike_rentals_2011.csv', sep=';', decimal=',')

rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()
#QC OK

rentals_2011
#Extra our firsr plot

rentals_2011.cnt
#The R way
np.mean (rentals_2011.cnt)
np.std(rentals_2011.cnt)

#The python way
rentals_2011.cnt.mean()
rentals_2011.cnt.describe()
rentals_2011.cnt.std()

#histogram
plt.hist(rentals_2011.cnt)
rentals_2011.cnt.hist() #Not this way

#Plot
x = rentals_2011['cnt']
plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0,7000, step=1000))
plt.title("Figure1. Registered rentals in Washington")
plt.ylabel('Frecuencia')
plt.xlabel('Number of rentals')
plt.show()

plt.hist(y ,edgecolor='black')
plt.show()

os.getcwd()
os.chdir('C:/Users/rafap/Desktop/EDEM/PEP/code_and_data')
os.getcwd()

weather_2011= pd.read_csv('weather_washington_2011.csv', sep=';', decimal=',')


weather_2011.shape
weather_2011.head()
weather_2011.tail()
weather_2011.dtypes
#QC OK

rentals_2011= pd.read_csv('washington_bike_rentals_2011.csv', sep=';', decimal=',')
rentals_weather_2011 =pd.merge(weather_2011, rentals_2011, on="day")


rentals_weather_2011.to_csv('rentals_weather_2011.csv') #Para guardar el fichero

del(rentals_weather_2011['dteday_y'])

rentals_weather_2011.rename(columns={'dteday_x': 'dteday'}, inplace = True)

#ADD NEW CASES

rentals_weather_2012 = pd.read_csv ("rentals_weather_2012.csv", sep=';', decimal=',')