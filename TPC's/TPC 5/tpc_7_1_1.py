# -*- coding: utf-8 -*-
"""
Created on Wed May  7 22:54:45 2025

@author: Utilizador
"""

from tpc_7_1 import Esfera

def main():
    
    radius = input("Diga o raio da esfera: ")
    vol=Esfera(radius)
    res1 = vol.area()
    print(res1)
   

main()
 