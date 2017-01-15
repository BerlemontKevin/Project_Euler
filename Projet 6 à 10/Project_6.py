# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:59:47 2015

@author: Kevin
"""

import numpy

sommecarre =0
carresomme = 0

for i in range(101):
    sommecarre = sommecarre + i*i
    carresomme=carresomme + i
    
print (carresomme*carresomme - sommecarre)