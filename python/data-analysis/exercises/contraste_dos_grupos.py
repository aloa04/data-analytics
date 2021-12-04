#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:22:23 2021

@author: pablobottero
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from pandas.api.types import CategoricalDtype

# Contraste de hipótesis - Cuali vs Cuanti
# 1. Describir variables
# 2. Hacer t.test
# 3. Hacer test grafico: plot of means

wbr.cnt.describe ()
plt.hist (wbr.cnt)