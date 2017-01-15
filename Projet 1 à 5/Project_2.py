# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:18:01 2015

@author: Kevin
"""

import numpy



l=[]
l.append(1)
l.append(2)

while(l[-1]+l[-2] <=4000000):
    l.append(l[-1]+l[-2])

print (sum(l*(1-numpy.fmod(l,2))))
print(l[-1])   
print(l[6])