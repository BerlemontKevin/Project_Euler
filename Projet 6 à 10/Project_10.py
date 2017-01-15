# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:45:59 2015

@author: Kevin
"""

from numpy import *
    
    
def premier(x):
    
    valeur = True
    entier = int(floor(sqrt(x)))
    i = 2
    while (valeur == True and i < entier+1):
            if (x != i):
                valeur = valeur and (mod(x,i) != 0)
            i = i+1  
            
    return valeur
    
    
def sum_prime(x) :
    sum =2    
    for i in range(3,x+1,2):
        if premier(i):
            sum = sum+i
    return sum
    
print (sum_prime(2000000))