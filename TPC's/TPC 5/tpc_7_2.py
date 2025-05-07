# -*- coding: utf-8 -*-
"""
Created on Wed May  7 23:11:18 2025

@author: Utilizador
"""

class Cube:
    def __init__(self, aresta):
        self.aresta = aresta
   
    def area(self):
        return self.aresta**2
     
    def sup(self):
        return (self.aresta**2) * 6
    
    def volume(self):
        return self.aresta**3
    
        