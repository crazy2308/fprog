# -*- coding: utf-8 -*-
"""
Created on Wed May  7 22:11:41 2025

@author: Utilizador
"""

class Esfera:
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return (self.radius ** 2 * 3,1416 * 4)

    def volume(self):
        return self.radius ** 3 * 4/3 * 3,1416

def main():
    
    radius = input("Diga o raio da esfera: ")
    vol=Esfera(radius)
    print(vol.volume())
    print(vol.area())

main()