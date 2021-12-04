# -*- coding: utf-8 -*-
import os
import pandas as pd    # gestionar datasets
import numpy as np     #gestionar numeros
import matplotlib.pyplot as plt      #  hacer gráficos

os.chdir('/Users/pablobottero/github/master/python/data_analysis/tasks/first_one')
print(os.getcwd())

songs = pd.read_csv('spotify.csv', sep=',' , decimal='.')
print(songs.head(10))

songs.shape
songs.head()
songs.tail()
songs.columns
#QC ok

print(songs.speechiness)
print(np.mean(songs.speechiness))
print(np.std(songs.speechiness))
print(songs.speechiness.describe())

#variables cuantitativas(media,desviacion y histograma)
      
x=songs['energy']
plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0,-9000, step=500))
plt.title("Figura 1. Energia de la canción")
plt.ylabel('Puntuación, en decimales')
plt.xlabel('De izquierda a derecha, canciones por popularidad')
plt.show()
plt.savefig('figura1.svg')

y=songs['danceability']
plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0,-9000, step=500))
plt.title("Figura 2. Bailabilidad de la canción")
plt.ylabel('Puntuación, en decimales')
plt.xlabel('De izquierda a derecha, canciones por popularidad')
plt.show()
plt.savefig('figura1.svg')

wbr = songs

#tabla de las variables a estudiar los cuales son cualitativos 
mytable = wbr.groupby(['energy']).size()

print(mytable)

#sumar los numeros de la variable
mytable2 = (mytable/n)*100
print(mytable2)

#redondear a un decimal 

print(round(mytable2,1))


bar_list = ['Sunny','Cloudy','rainy']

plt.bar(bar_list,mytable2,edgecolor='black')
plt.ylabel('percentaje')
plt.title('percentaje of weather situation')
plt.text(1.7, 50,'n: 731')

plt.savefig('bar1.svg')
plt.savefig('bar1.jpg')

print(wbr.tail())
