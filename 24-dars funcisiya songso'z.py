# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:50:09 2021

@author: Admin
"""

import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))


product = lambda x, y : x ** y
print(product(3, 2))


def daraja(n):
    return lambda x : x**n



kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")



from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))




sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz



kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)



kvadratlar = []
for son in sonlar:
    kvadratlar.append(son*son)
    
    
a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)


ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))


import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)



import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)



mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)




mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)


list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))



