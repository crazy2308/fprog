#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import *
from salav2 import *
from classes import waiter
def tier1():
    # Cria a janela gráfica
    sala_obj = Sala()
    sala_obj.run("salaxx.txt")
    robo = waiter(sala_obj.win, Point(97, 145), 5, 100)
    robo.desenhar()

    win.getMouse()
    win.close()

tier1()