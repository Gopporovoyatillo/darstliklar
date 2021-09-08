# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:46:10 2021

@author: ACER
"""


import math

class Nuqta:
    """Nuqta klassi"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __call__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Nuqta: x={self.x}, y={self.y}"
    
    def __sub__(self,boshqa):
        A = (self.x, self.y)
        B = (boshqa.x, boshqa.y)
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(A, B)]))

    
nuqtaA = Nuqta(0,0)
nuqtaB = Nuqta(3,4)
print(nuqtaA-nuqtaB)