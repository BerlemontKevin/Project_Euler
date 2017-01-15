# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:40:39 2015

@author: Kevin
"""

import numpy
    
    
def premier(x):
    
    valeur = True
    for i in range(2,x):
        if (valeur == True) and (x != i):
            valeur = valeur and (mod(x,i) != 0)
        
            
    return valeur
    
    
    

resultat = 1
i=1
while (i < numpy.floor(numpy.sqrt(600851475143))):
    if (mod(600851475143,i)==0) and (premier(i) == True) :
        resultat =i
    
    i=i+1
    
print (resultat)
print (premier(2))