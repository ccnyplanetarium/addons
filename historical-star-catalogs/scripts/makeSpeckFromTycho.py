#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 1 10:41 2020

@author: James Hedberg
"""

import pandas as pd
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import Latitude, Longitude  # Angles

#data set can be found here: https://www.aanda.org/articles/aa/abs/2010/08/aa14002-10/aa14002-10.html

filename = 'keplere.dat'
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


data = pd.read_csv(filename, sep='\s+', header=None, nrows = 1006)

for index, row in data.iterrows():
    #print(index);
    
    #set -1 for latitude if in the australis hemisphere (A)
    
    if row[11] == 'A':
        signLat = -1
    else :
        signLat = 1

    # Longitudes are measured as degrees from a zodic sign, which is in column [6] of the data
    
    ra = Longitude(((row[6]-1)*30+row[7],row[8]), unit=u.deg)
    dec = Latitude((signLat*row[9],row[10]), unit=u.deg)
    
    #The Equinox of 1601 is chosen for the Tycho Data Set.
    
    object = SkyCoord(ra,dec,distance=10*u.pc, frame='geocentrictrueecliptic', equinox='+01601-01-01T12:00:00.0')

    astar = " "+str(object.galactic.cartesian.x.value)+" "+ \
          str(object.galactic.cartesian.y.value)+" "+ \
          str(object.galactic.cartesian.z.value)+" "+ \
          str(.5)+" "+\
          str(row[12])+" "+\
          str(row[12])+" "+\
          str(row[12])+" "
    
    astarLabel = " "+str(object.galactic.cartesian.x.value)+" "+ \
          str(object.galactic.cartesian.y.value)+" "+ \
          str(object.galactic.cartesian.z.value)+" "+ \
          "text "+str(row[4])+"-"+str(row[13])+" "
          
    lines.append(astar)
    labellines.append(astarLabel)


# save the speck files for the stars and labels

afile = open('tycho.speck', 'w')
afile.write("datavar 0 colorb_v \n"+"datavar 1 lum \n"+"datavar 2 absmag \n"+"datavar 3 appmag \n")
for line in lines:
    afile.write("%s\n" % line)

afile.close()

afile2 = open('tycho_labels.label', 'w')
afile2.write("textcolor 1 \n")
for line in labellines:
    afile2.write("%s\n" % line)

afile2.close()

