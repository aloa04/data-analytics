#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name = ['Troy', 'Rafa', 'Olimpia']
age = [20,21,23]
gender = ['Male', 'Male', 'Female']

print(name, age, gender)

class2021 = pd.DataFrame({'name' : name, 'age' : age, 'gender' : gender})

#del (age,)

class2021.shape()
class2021.head(3)
class2021.tail(4)

edad = class2021.age

del(edad)

os.getcwd()