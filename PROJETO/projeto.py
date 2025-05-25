#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import *
from menu_principal import menu_principal

def tier1():
    # Cria a janela gráfica
    sala = Sala()
    sala.run("salaxx.txt")

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, sala.x1, sala.y1, sala.x2, sala.y2)

    while True:
        click = sala.win2.getMouse()
        # Verifica se clicou no botão SAIR
        if sala.saida and Button.is_click_in_button(click, sala.saida.button):
            sala.win2.close()
            # Reabre o menu principal
            game = menu_principal()
            game.run()
            break
        else:
            robo.move_to_point(click)