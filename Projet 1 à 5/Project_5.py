# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:01:36 2015

@author: Kevin
"""

from math import gcd
def ppcm(N):
    p = 1                      # initialise ppcm des n 1ers entiers > 0
    for n in range(2,N+1):     # de n=2 à n=N
        p = n*p // gcd(n, p)   #   nouvelle valeur de p=ppcm(1,...,n)
    return p                  # renvoie le ppcm de 1,...,N
    
print (ppcm(20))
