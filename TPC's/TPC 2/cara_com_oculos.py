# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:33:11 2025

@author: Utilizador
"""

from graphics import GraphWin, Circle, Point, Oval, Polygon, Line

def main(): 
    
    win = GraphWin("Que cara bonita!", 500, 500)
    win.setCoords(0, 0, 100, 100)
       
    #cara
    cara = Circle(Point(50, 50), 25)
    cara.setFill("salmon")
    cara.setOutline("black")
    cara.draw(win)
    
    #olhos
    olhoe = Oval(Point(34,56), Point(46,66))
    olhoe.setFill("White")
    olhoe.setOutline("black")
    olhoe.draw(win)
    
    olhod = Oval(Point(54,56), Point(66,66))
    olhod.setFill("White")
    olhod.setOutline("black")
    olhod.draw(win)
    
    #pupila
    pupilae = Circle(Point(40,61), 2)
    pupilae.setFill("black")
    pupilae.draw(win)
    
    pupilad = Circle(Point(60,61), 2)
    pupilad.setFill("black")
    pupilad.draw(win)
    
    #orelhas
    orelhae = Polygon(Point(74,60), Point(80,60), Point(74,40))
    orelhae.setFill("salmon")
    orelhae.setOutline("black")
    orelhae.draw(win)
   
    orelhad = Polygon(Point(26,60), Point(20,60), Point(26,40))
    orelhad.setFill("salmon")
    orelhad.setOutline("black")
    orelhad.draw(win)
   
    #nariz
    nariz = Polygon(Point(45,45), Point(55,45), Point(50,60))
    nariz.setFill("orange")
    nariz.setOutline("black")
    nariz.draw(win)
    
    #boca
    boca = Oval(Point(40, 30), Point(60,35))
    boca.setFill("red")
    boca.draw(win)
    
    win.getMouse()
    
    #oculos
    
    oculoe = Circle(Point(40,61), 9)
    oculoe.setFill("black")
    oculoe.draw(win)
    
    oculoe = Circle(Point(60,61), 9)
    oculoe.setFill("black")
    oculoe.draw(win)
    
    haste =  Line(Point(23, 60.5), Point(77,60.5))
    haste.setOutline("black")
    haste.draw(win)
    
    
    win.getMouse()
    win.close()
    
main()