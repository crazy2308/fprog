#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import * # Importa as classes necessárias
from menu_principal import menu_principal # Importa o menu principal

def tier1(): #Executa o primeiro tier do robo
    sala = Sala() # Cria uma instância da classe Sala
    sala.run("sala49.txt") # Carrega a sala a partir do ficheiro "sala49.txt"

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, sala.posicoes_mesa, sala.posicoes_Div)
  
    robo.go_to_table_tier1(sala.mesas) # Move o robô para a mesa do tier 1

    while True: 
        click = sala.win2.getMouse() #deteta o clique do rato

        # Verifica se clicou no botão SAIR
        if sala.saida and Button.is_click_in_button(click, sala.saida.button):
            sala.win2.close()
            game = menu_principal()
            game.run()
            break


def tier2(): #Executa o segundo tier do robo
    sala = Sala()
    sala.run("sala49.txt")

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, sala.posicoes_mesa, sala.posicoes_Div)
    robo.mostrador(robo.battery_level) # Mostra o nível da bateria do robô
    while True:
        click = sala.win2.getMouse()

        if sala.saida and Button.is_click_in_button(click, sala.saida.button):
            sala.win2.close()
            game = menu_principal()
            game.run()
            break

        clicou_em_mesa = robo.go_to_table_tier2(click, sala.mesas) # Detecta se o clique foi numa mesa
        
        if not clicou_em_mesa:
            robo.obstaculo(click) # Se não clicou numa mesa, cria um obstáculo
        else:
            print("Robô movido para a mesa.")

def tier3(): #Executa o terceiro tier do robo
    sala = Sala()
    sala.run("sala49.txt")

    robo = Waiter(sala.win2, Point(97, 145), 4, 100, sala.posicoes_mesa, sala.posicoes_Div)
    robo.mostrador(robo.battery_level)
    while True:
        click = sala.win2.getMouse()

        # Verifica se clicou no botão SAIR
        if sala.saida and Button.is_click_in_button(click, sala.saida.button):
            sala.win2.close()
            game = menu_principal()
            game.run()
            break

        clicou_em_mesa = robo.go_to_table_tier3(click, sala.mesas)
        
        if not clicou_em_mesa:
            robo.obstaculo(click)
        else:
            print("Robô movido para a mesa.")
