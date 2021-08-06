# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:36:12 2021

@author: Admin
"""

import funksia
avto1=funksia.avto_info('gm', 'matiz', 'choko', 'mehanika', 2008,4000)
funksia.info_print(avto1)

# modulni qisqartirish
import funksia as fu
avto1=fu.avto_info('gm', 'matiz', 'choko', 'mehanika', 2008,4000)
fu.info_print(avto1)


# moduldan faqat kerakli funkisyani tanlab olish
from funksia import avto_info, info_print
avto1=avto_info('gm', 'matiz', 'choko', 'mehanika', 2008,4000)
info_print(avto1)

#funksiani qisqartirish
from funksia import avto_info as ai, info_print as ip
avto1=ai('gm', 'matiz', 'choko', 'mehanika', 2008,4000)
ip(avto1)


from funksia import*
avto1=avto_info('gm', 'matiz', 'choko', 'mehanika', 2008,4000)
info_print(avto1)

import math

x=400
print(math.sqrt(x))
print(pow(5,5))
from math import pi
print(pi)
print(math.log2(8))
print(math.log10(100))

#math ichidagi ayrim funksiyalar
#Funksiya          Funksiya ta'rifi
#ceil(x)           x dan katta yoki teng bo'lgan eng kichik butun sonni qaytaradi
#fabs(x)           x ning absolyut qiymatini qaytaradi
#floor(x)          x dan kichik yoki teng bo'lgan eng yaqin butun sonni qaytaradi
#exp(x)            xe ni qaytaruvchi funksiya
#cos(x)            cosinus (x) ni qaytaruvchi funksiya
#sin(x)            sinusnini(x) qaytaruvchi funksiya
#tan(x)            tan(x) ni qaytaruvchi funksiya
#degrees(x)        x burchakning radian qiymatini darajaga konvertasiya qilish
#radians(x)        x burchakning daraja qiymatini radianga konvertasiya qilish 
#ellipsis()        Matematik konstanta  (2.71828...)


import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)



ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz


x = list(range(0,51,5))
print(x)
print(r.choice(x))


x = list(range(11))
print(x)
r.shuffle(x)
print(x)

