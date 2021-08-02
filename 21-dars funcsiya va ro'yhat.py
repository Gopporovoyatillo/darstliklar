# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:32:12 2021

@author: Admin
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(talabalar)

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(talabalar)

