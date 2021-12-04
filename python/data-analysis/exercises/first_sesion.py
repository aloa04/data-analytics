#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


name=['Yaling','Sofia', 'Maria','Pablo','Ines']
age = [28,23,25,23,25]
gender= ['Female','Female', 'Female','Male','Female']

print(name,age,gender)


class2021 = pd.DataFrame({'name':name, 'age':age, 'gender': gender})
print(class2021)

#Clean up
del (name, gender, age)

class2021.shape #Dimension
class2021.head(3)
class2021.tail(2)
#QC OK

edad = class2021.age
del(edad)


#Get working directory
os.getcwd()

#Change working directory
os.chdir()
os.getcwd()

#Save dataframe
class2021.to_excel("class2020.xlsx")
class2021.to_csv("class2020.csv")


class2021.age.hist()