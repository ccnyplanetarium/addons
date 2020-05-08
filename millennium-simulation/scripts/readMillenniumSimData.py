#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:34:28 2020

@author: james
"""

import pandas as pd
import numpy as np
#download ascii data files here:
#https://wwwmpa.mpa-garching.mpg.de/galform/agnpaper/

#put it somewhere

filename = 'data/croton_etal.ugriz.ascii'


#get the number of rows (if you want to skip some during import)
def sum1forline(filename):
    with open(filename) as f:
        return sum(1 for line in f)
#this gets the number of rows
nRows = sum1forline(filename)
print('number of rows: ' + str(nRows))


#define the rows to skip
skip = np.arange(nRows)
skip = np.delete(skip, np.arange(0, nRows, 5))

#read the csv
#only use the first three columns for position data - could do more if interested in other parameters
#and skip the rows defined above

data = pd.read_csv(filename, engine='python', header=None, delim_whitespace=True, names=['xPos', 'yPos', 'zPos'], usecols=[0,1,2], skiprows = skip)



#or only read the first n rows
#   data = pd.read_csv(filename, engine='python', header=None, delim_whitespace=True, names=['xPos', 'yPos', 'zPos'], usecols=[0,1,2], nrows = 10000)


#save as csv
data.to_csv('millennium10k.speck',sep=" ", index=False)
