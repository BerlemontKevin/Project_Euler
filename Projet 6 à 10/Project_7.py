# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:02:22 2015

@author: Kevin
"""
from numpy import *
def premier(x):
    
    valeur = True
    entier = int(floor(sqrt(x)))
    for i in range(2,entier+1):
        if (valeur == True) and (x != i):
            valeur = valeur and (mod(x,i) != 0)
        
            
    return valeur
    
nombre = 1
test=2    
while (nombre < 10001):
    test = test+1
    if premier(test):
        nombre = nombre + 1
                    
        
print (test)