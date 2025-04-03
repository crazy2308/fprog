# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 18:38:08 2025

@author: Utilizador
"""

from graphics import GraphWin, update, Point
from Face import Face

def main():
    
    #janela
    win = GraphWin("Animaçao circulo", 800, 600, autoflush=False)
    win.setCoords(0, 0, 800.0, 600.0)
    cara = Face(win, Point(400, 300), -20)
    dx = 2
    dy = 2
    #loop de animacao
    for i in range (144*20):

        meio = cara.getCenter()
        x = meio.getX()
        y = meio.getY()
        
        if 0 > (x - 10) or (x + 10) > 800:
            dx = -dx
            
        if 0 > (y - 10) or (y+10) > 600:
            dy = -dy
        
        
        cara.move(dx, dy)
        update(144)
       
    win.getMouse()
    win.close()
         
    
main()
