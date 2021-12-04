#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from pandas.api.types import CategoricalDtype
import scipy.stats as stats
import seaborn as sns

os.chdir('/Users/pablobottero/github/master/python/data_analysis')

wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
print(wbr.shape)

#añado una columna que es un ratio que yo he decidido crear
wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)
print(wbr.shape)
wbr.cs_ratio.describe()

#elimino cnt pa volver a crearla pq sabemos que es la suma de otras dos columnas
del wbr['cnt']
wbr['cnt'] = (wbr.casual)+(wbr.registered)
 
#RECODIFICAR VARIABLES
#En este caso estamos creando una anueva columna con las estaciones en base a la columna 
#ya existente que esta codificada
wbr.loc[(wbr['season']==1),"season2"] = "Winter"
wbr.loc[(wbr['season']==2),"season2"] = "Spring"
wbr.loc[(wbr['season']==3),"season2"] = "Summer"
wbr.loc[(wbr['season']==4),"season2"] = "Fall"

#Quality control
pd.crosstab(wbr.season, wbr.season2)
 
#otra recodificacion
wbr.loc[(wbr['cnt']<2567), "cnt2"]= "1: low rentals"
wbr.loc[(wbr['cnt']>=2567) & (wbr['cnt']<6442), "cnt2"]= "2: average rentals"
wbr.loc[(wbr['cnt']>=6442), "cnt2"]= "3: high rentals"
 
#quality control
plt.scatter(wbr.cnt, wbr.cnt2)

#frecuencias
mytable = pd.crosstab(index=wbr["cnt"], columns="count")
print(mytable)

#porcentajes
n=mytable.sum()
mytable2= (mytable/n)*100
plt.bar(mytable2.index, mytable2['count'])

wbr.loc[ (wbr['cnt']<2567.1) ,"cnt_cat2"]= "Low rentals" 
wbr.loc[ ((wbr['cnt']>2567.1) & (wbr['cnt']<6441.6)) ,"cnt_cat2"]= "Average rentals" 
wbr.loc[ (wbr['cnt']>6441.6) ,"cnt_cat2"]= "High rentals"

# Para saber que tipo de datos hay
wbr.dtypes

 # ------

my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat5"] = wbr.cnt_cat2.astype(my_rentals_type)

wbr.dtypes

# Contraste de hipótesis - Cuali vs Cuanti
# 1. Describir variables
# 2. Hacer t.test
# 3. Hacer test grafico: plot of means

wbr.cnt.describe ()
plt.hist (wbr.cnt)
myTable = pd.crosstab(index=wbr["wd_cat"], columns="count")
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')
plt.show

wbr.groupby('workingday').cnt.mean()

#Comparación estadística
#Extraer el numero de alquileres cnt para días laborables y no laborables

cnt_wd = wbr.loc[wbr.workingday==1, "cnt"]
cnt_nwd = wbr.loc[wbr.workingday==0, "cnt"]


#Si ponemos el = es para guardar la variable
res=stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
print (res)

'''
print (res[1]) para sacar solo el resultado p.value

p.value es la probabilidad de que las diferencias que observamos se deban al 
azar o al error del muestreo, en realidad no haya ningún efecto en el test 
que estoy haciendo

En este caso la probabilidad es del 11% -> pvalue=0.11005737827017054 y las 
diferencias de la muestra causan riesgo de que se deba al error del muestreo
Como el pvalue es superior al 5%, los dias no tienen valor en las ventas
'''

#Descriptive comparison: 
wbr.groupby('workingday').cnt.mean()
#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_wd=wbr.loc[wbr.workingday=='Yes', "cnt"]
cnt_nwd=wbr.loc[wbr.workingday=='No', "cnt"] 
#Perform a t test for mean comparison
#import scipy.stats as stats
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)


#CI meanplot - V1
plt.figure(figsize=(5,5))
ax = sns.pointplot(x='workingday', y='cnt',  data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle="round", facecolor="white",lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')


#Plotmeans
plt.figure(figsize=(5,5))
ax=sns.pointplot(x="yr",y="cnt",data=wbr,ci=95,join=0)
ax.set_ylabel('')
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), 
            linewidth=1, 
            linestyle= 'dashed',
            color="indigo")
props = dict(boxstyle='square', facecolor='peachpuff', lw=0.5)
plt.xticks((0,1), ("2011", "2012"))
plt.xlabel('Year')
plt.title('Figure 7. Average rentals by Year.''\n')
plt.text(-0.35,5400,'Mean:4504.3''\n''n:731' '\n' 't:18.6' '\n' 'Pval.: 0.000',bbox=props)


##Descriptive comparison ANOVA
wbr.groupby('weathersit').cnt.mean()
#Statistical comparison
cnt_sunny=wbr.loc[wbr.weathersit=='1', "cnt"]
cnt_cloudy=wbr.loc[wbr.weathersit=='2', "cnt"]
cnt_rainy=wbr.loc[wbr.weathersit=='3', "cnt"]
stats.f_oneway(cnt_sunny, cnt_cloudy,cnt_rainy )

mytable = pd.crosstab(index=wbr["weathersit"])

#Graphic comparison: confidence intervals for the means
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="weathersit", y="cnt", data=wbr, capsize=0.05, ci=95.0, join=0) #parámetro de confianfianza
ax.set_ylabel('')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=wbr.cnt.mean(), 
            linewidth=1, 
            linestyle= 'dashed',
            color="green")
props = dict(boxstyle='square', facecolor='peachpuff', lw=0.5)
plt.text(1.5, 5000, 'Mean: 4504.3''\n''n: 731' '\n' 'F: 40.06' 
'\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 8. Average rentals by Weather Situation.''\n')
plt.savefig('prueba.svg')
plt.show()

sns.boxplot(x='weathersit', y="CNT", data=wbr)





