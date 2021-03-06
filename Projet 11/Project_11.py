# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:33:09 2015

@author: Kevin
"""

from numpy import *

from Project_11_matrice import matrice


def produit_grille(matrice):
    dim = len(matrice)
    grid = array(matrice)
    r, r3 = range(dim), range(dim-3)
    m1 = max(prod(grid[i,j:j+4]) for i in r for j in r3)
    m2 = max(prod(grid[i:i+4,j]) for i in r3 for j in r)
    m3 = max(prod(diag(grid[i:i+4,j:j+4])) for i in r3 for j in r3)
    m4 = max(prod(diag(grid[i:i+4,j+4:j:-1])) for i in r3 for j in r3)
    return max(m1,m2,m3,m4)
    
print (produit_grille(matrice))
