#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 22 09:38 2020

@author: James Hedberg
"""

import pandas as pd
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import Latitude, Longitude

#data set can be found here: http://www.etwright.org/astro/almagest.html

filename = 'cat1.csv'
lines=[]
labellines=[]
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


data = pd.read_csv(filename, sep=',', header=None, delim_whitespace=False, nrows = 1027)

for index, row in data.iterrows():
    #print(index);
    ra = Longitude((row[3],row[4],0), unit=u.deg)
    dec = Latitude((row[5],row[6],0), unit=u.deg)

    #Equinox of 58AD is chosen for the data based on best estimates. 
    object = SkyCoord(ra,dec,distance=10*u.pc, frame='geocentrictrueecliptic', equinox='+00058-01-01T12:00:00.0')

    astar = " "+str(object.galactic.cartesian.x.value)+" "+ \
          str(object.galactic.cartesian.y.value)+" "+ \
          str(object.galactic.cartesian.z.value)+" "+ \
          str(.5)+" "+\
          str(row[7])+" "+\
          str(row[7])+" "
    
    astarLabel = " "+str(object.galactic.cartesian.x.value)+" "+ \
          str(object.galactic.cartesian.y.value)+" "+ \
          str(object.galactic.cartesian.z.value)+" "+ \
          "text "+str(row[11])+"-"+str(row[10])+" "
          
    lines.append(astar)
    labellines.append(astarLabel)


# save the speck files for the stars and labels

afile = open('almagest.speck', 'w')
afile.write("datavar 0 colorb_v \n"+"datavar 1 lum \n"+"datavar 2 absmag \n"+"datavar 3 appmag \n")
for line in lines:
    afile.write("%s\n" % line)

afile.close()

afile2 = open('almagest_labels.label', 'w')
afile2.write("textcolor 1 \n")
for line in labellines:
    afile2.write("%s\n" % line)

afile2.close()
