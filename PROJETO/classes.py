#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro cria todas as funções e classes e precisamos para definir o projeto final

from graphics import *
from math import *

class waiter:
    def __init__(self, window, center_point, body_radius, battery_level):
        self.window = window
        self.center = center_point
        self.body_radius = body_radius
        self.battery_level = battery_level
        self.ignore_collisions = False  # Só ignora colisões quando ativado

        # Cria o corpo do robô (círculo cinzento claro)
        self.body = Circle(self.center, self.body_radius)
        self.body.setFill(color_rgb(200, 200, 200))
        self.body.draw(self.window)

        # Cria o indicador de bateria (círculo verde)
        battery_radius = self.body_radius / 4
        self.battery = Circle(self.center, battery_radius)
        self.battery.setFill(color_rgb(0, 255, 0))
        self.battery.draw(self.window)

        
class Button: # Cria um botão 
    @staticmethod
    def is_click_in_button(point, button):
        p1 = button.getP1()
        p2 = button.getP2()
        return p1.getX() < point.getX() < p2.getX() and p1.getY() < point.getY() < p2.getY()

    @staticmethod
    def create_button(win, p1, p2, label_text):  
        button = Rectangle(p1, p2)
        button.draw(win)
        label = Text(button.getCenter(), label_text)
        label.draw(win)
        return button, label  # Retorna o objeto label ao invés do texto