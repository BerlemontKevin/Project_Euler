# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:52:16 2015

@author: Kevin
"""

from numpy import *

def paladindrome():
    r = range(900,999)
    
    return(max(x*y for x in r for y in r if str(x*y) == str(x*y)[:-1]))
    
    
print (palindrome())