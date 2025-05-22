#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import *

def tier1():
    # Cria a janela gráfica
    win = GraphWin("Zé das Bifanas", 800, 600) 
    win.setCoords(0, 600, 800, 0)
    win_bg = Image(Point(400, 300), "azuleijo.png").draw(win)
    robo = waiter(win, Point(20, 20), 20, 100)

    win.getMouse()
    win.close()