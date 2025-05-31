#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import *
from menu_principal import menu_principal

def tier1():
    sala = Sala()
    sala.run("sala49.txt")
    posicoes_mesa = sala.devolver_mesas()

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, sala.x1, sala.y1, sala.x2, sala.y2, posicoes_mesa)
  
    robo.go_to_table_tier1(sala.mesas)

    while True:
        click = sala.win2.getMouse()

        # Verifica se clicou no botão SAIR
        if sala.saida and Button.is_click_in_button(click, sala.saida.button):
            sala.win2.close()
            game = menu_principal()
            game.run()
            break


def tier2():
    sala = Sala()
    sala.run("sala49.txt")

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, sala.x1, sala.y1, sala.x2, sala.y2, sala.posicoes_mesa)
    while True:
        click = sala.win2.getMouse()

        # Verifica se clicou no botão SAIR
        if sala.saida and Button.is_click_in_button(click, sala.saida.button):
            sala.win2.close()
            game = menu_principal()
            game.run()
            break

        clicou_em_mesa = robo.go_to_table_tier2(click, sala.mesas)
        
        if not clicou_em_mesa:
            robo.obstaculo(click)
        else:
            print("Robô movido para a mesa.")
