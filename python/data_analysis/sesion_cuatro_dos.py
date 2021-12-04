import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

os.chdir('/Users/pablobottero/github/master/python/data_analysis')
  
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
print(wbr.shape)

#Subsetting -> seleccionar variables
my_vars=['temp_celsius','cnt']  #variables con las que me quiero quedar
wbr_minimal= wbr[my_vars] #aqui creo una nueva variable con el csv de solo las variables escogidas
print(wbr_minimal.shape)

mytable= wbr.groupby(['yr']).size()  #con esto miro cuantos años estudia mis datos
print(mytable)

n = mytable.sum()
mytable2 = (mytable/n)*100  #saco porcentajes
print(mytable2)
 
#subset año 0

wbr_2011=wbr[wbr.yr == 0]
 
plt.hist(wbr_2011.cnt)
print(wbr_2011.cnt.describe())
 
wbr_winter12 = wbr[(wbr.yr == 1) & (wbr.season == 1)]  #aqui estamos estableciendo la condicion de que solo me sauqe los datos de invierno de 2012
#LAS CONDICIONES VAN EN PARENTESIS SIEMPRE
print(wbr_winter12.shape)
plt.hist(wbr_winter12.cnt)
print(wbr_winter12.cnt.describe())
   
#ventas de invierno y otoño
wbr_wo = wbr[(wbr.season == 1) | (wbr.season == 4)]
print(wbr_wo.shape)
plt.hist(wbr_wo.cnt)
print(wbr_wo.cnt.describe()) 