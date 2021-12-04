#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 16:58:35 2021

@author: pablobottero
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from pandas.api.types import CategoricalDtype
import scipy.stats as stats
import seaborn as sns

os.chdir('/Users/pablobottero/github/master/python/data_analysis/tasks/second_one/')

#Abrir fichero
rank = pd.read_csv('billionaires_index.csv', sep=',', decimal=',')
print(rank.shape)
rank

#Obtener las personas de España de la lista
rank[rank["Country"] == "Spain"]

#Crear un fichero con los 50 primeros para trabajar con ellos
rank.head(50).to_csv("50b.csv")
bsl = pd.read_csv('50b.csv', sep=',', decimal=',') # Billionaire Sorted List

#Agrupar valores por industria y país
ig = bsl['Industry'].value_counts()
cg = bsl['Country'].value_counts()

ig.to_csv("industries.csv")
cg.to_csv("countries.csv")
bsl_ig = pd.read_csv('industries.csv', sep=',', decimal=',')
bsl_cg = pd.read_csv('countries.csv', sep=',', decimal=',')

#QC_done

# Imprimir un gráfico con el listado de  billonarios por industria
bsl.Industry.describe()
plt.hist (bsl.Industry)
i_table = pd.crosstab(index=bsl["Industry"], columns="count")
n=i_table.sum()
i_table2 = (i_table/n)*100
print(i_table2)
plt.bar((i_table.index), i_table['count'])
plt.xlabel('Industries')
plt.ylabel('%')
plt.title('Figure 2. Percentaje of billionaires \n by industry.')
plt.savefig('grafica.svg')
plt.show

#QC_done

# Imprimir un gráfico con el listado de  billonarios por pais
bsl_cg.Country:Number.describe()
plt.hist (bsl_cg.Country)
c_table = pd.crosstab(index=bsl["Country"], columns="count")
n=c_table.sum()
c_table2 = (c_table/n)*100
print(c_table2)
plt.bar(c_table2.index, c_table2['count'])
plt.xlabel('Industries')
plt.ylabel('%')
plt.title('Figure 1. Percentaje of billionaires \n by industry.')
plt.show

print(c_table.sort())
-----------------------
#Hacer graficos también por países
#Analizar los porcentajes por país y por industria
#Sacar el pocentaje de españoles en la lista completa
#Obtener los porcentajes de ricos por país en comparación con la lista (500)







































