# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:34:37 2021

@author: ACER
"""

class Talaba:
    def __init__(self,ism,familya,tyil,telnem):
        self.ismi=ism
        self.famsi=familya
        self.yili=tyil
        self.nomeri=telnem
        
        
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ismi
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.famsi
    
    def get_age(self):
        """Talabaning yoshini qaytaradi"""
        return self.yili
    
    def get_number(self):
        """Talabaning tel no'merini qaytaradi"""
        return self.nomeri
        
    def get_old(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil- self.yili
    
        
        
        
    def tanishtir(self):
        return f"ismim {self.ismi} familyam {self.famsi} tug'ilgan yilim {self.yili} no'merim {self.nomeri}"


        
        
talaba0=Talaba("Oyatillo","G'opporov",1997,"+998911234567")
talaba1=Talaba("husniddin"," jumamurodov",1994,"+998911234568")
talaba2=Talaba("muhammadsolih","hakimov",2000,"+998911121122")
talaba4=Talaba("oyatillo","boyuzoqov",1996,"+9989112365655")


print(talaba0.get_old(2021))
print("Alhamdulillah ")