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

filename = 'ptolema.dat'
lines=[]
labellines=[]
brightnessFixed = 0.0
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
#setup the widths of the columns as described here: http://cdsarc.u-strasbg.fr/viz-bin/ReadMe/J/A+A/544/A31?format=html&tex=true
widths = [
    4, # 0 Sequence number in Ptolemaios Catalogue
    3, # 1 Constellation sequence number
    2, # 2 [=]
    3, # 3 Abbreviation of constellation name
    3, # 4 Sequence number of star in constellation
    1, # 5 'a' for star outside the constellation figure
    4, # 6 [1/12] Zodiacal sign of longitude
    3, # 7 [0/30] Longitude (degrees)
    3, # 8 [0/59] Longitude (arcmin) 
    4, # 9 [0/90] Ecliptic latitude (degrees)
    3, # 10 [0/60] Ecliptic latitude (arcmin)
    2, # 11 Sign of latitude
    3, # 12 Magnitude as given by Ptolemaios
    1, # 13 [bf] brighter/fainter qualifier by Ptolemaios
    7, # 14 Hipparcos number of identification
    2, # 15 [1,6] Quality of identification
    
]

#read in the fixed width file using the defined widths

data = pd.read_fwf(filename, header=None, widths=widths, nrows = 1027)
print(data)

for index, row in data.iterrows():
    print(index);
    
    #set -1 for latitude if in the australis hemisphere (A)
    
    if row[11] == 'A':
        signLat = -1
    else :
        signLat = 1
        
    brightness = str(row[12])
    #print(row[12])

    #account for brightness modifier, if '.' then make a little dimmer, if ':' then make a little brighter
    if row[13] == 'f' :
        brightnessFixed = float(brightness)+.3
    elif row[13] == 'b' :
        brightnessFixed = float(brightness)-.3
    else :
        brightnessFixed = float(brightness)
    #brightnessFixed = brightness.translate(None, string.punctuation)

    # Longitudes are measured as degrees from a zodic sign, which is in column [7] of the data
    
    ra = Longitude(((row[6]-1)*30+row[7],row[8]), unit=u.deg)
    dec = Latitude((signLat*row[9],row[10]), unit=u.deg)
    
    #The Equinox of 1601 is chosen for the Tycho Data Set.
    
    object = SkyCoord(ra,dec,distance=10*u.pc, frame='geocentrictrueecliptic', equinox='+00058-01-01T12:00:00.0')

    astar = " "+str(object.galactic.cartesian.x.value)+" "+ \
          str(object.galactic.cartesian.y.value)+" "+ \
          str(object.galactic.cartesian.z.value)+" "+ \
          str(.5)+" "+\
          str(brightnessFixed)+" "+\
          str(brightnessFixed)+" "+\
          str(brightnessFixed)+" "
    
    astarLabel = " "+str(object.galactic.cartesian.x.value)+" "+ \
          str(object.galactic.cartesian.y.value)+" "+ \
          str(object.galactic.cartesian.z.value)+" "+ \
          "text "+str(row[5])+"-"+str(row[6])+" "
          
    lines.append(astar)
    labellines.append(astarLabel)


# save the speck files for the stars and labels

afile = open('ptolemy.speck', 'w')
afile.write("datavar 0 colorb_v \n"+"datavar 1 lum \n"+"datavar 2 absmag \n"+"datavar 3 appmag \n")
for line in lines:
    afile.write("%s\n" % line)

afile.close()

afile2 = open('ptolemy_labels.label', 'w')
afile2.write("textcolor 1 \n")
for line in labellines:
    afile2.write("%s\n" % line)

afile2.close()

