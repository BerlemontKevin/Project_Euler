# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:05:45 2015

@author: Kevin
"""

import numpy

somme = 0
for i in range(1,1000):
    if (numpy.fmod(i,3) == 0) or (numpy.fmod(i,5) ==0):
        somme = somme+i
        
print (somme)