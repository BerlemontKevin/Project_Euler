# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:40:04 2015

@author: Kevin
"""

from numpy import *

def isquare(x):
    return (floor(sqrt(x))**2 == x)



for i in range(500):
    for j in range(500):
        if (i**2 + j**2 == (1000 -i-j)**2):
            product =i*j*(1000-i-j)
            
print (product)