#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import *

def tier1():
    # Cria a janela gráfica
    sala = Sala()
    sala.run("salaxx.txt")

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, 0, 0, 150, 150)

    while True:
        click = sala.win2.getMouse()
        if click:  # Se houve clique
            robo.move_to_point(click)