#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:14:18 2021

@author: pablobottero
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
  
os.chdir('/Users/pablobottero/github/master/python/data_analysis')
  
wbr = pd.read_csv('wbr_ue.csv', sep=';', decimal=',')
print(wbr.shape)