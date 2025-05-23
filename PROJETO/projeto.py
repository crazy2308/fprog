#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro é a implementação dos 3 tiers do robo

from graphics import *
from classes import *
from salav2 import *
from classes import waiter
def tier1():
    # Cria a janela gráfica
<<<<<<< HEAD
    sala_obj = Sala()
    sala_obj.run("salaxx.txt")
    robo = waiter(sala_obj.win, Point(97, 145), 5, 100)
    robo.desenhar()

    win.getMouse()
    win.close()

tier1()
=======
    win = GraphWin("Zé das Bifanas", 800, 600) 
    win.setCoords(0, 600, 800, 0)
    win_bg = Image(Point(400, 300), "azuleijo.png").draw(win)
    robo = Waiter(win, Point(20, 20), 20, 100)

    while True:
        click = win.getMouse()
        if click:  # Se houve clique
            robo.move_to_point(click)
>>>>>>> 157aa76fedc8b48dcc7bbfaac98f20ed84b713b9
