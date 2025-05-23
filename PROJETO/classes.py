#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro cria todas as funções e classes e precisamos para definir o projeto final

from graphics import *
from math import *

from salav2 import *

from time import *

class Waiter:
    def __init__(self, window, center_point, body_radius, battery_level):
        self.window = window
        self.center = center_point
        self.body_radius = body_radius
        self.battery_level = battery_level
        self.ignore_collisions = False  # Só ignora colisões quando ativado

        # Cria o corpo do robô (círculo cinzento claro)
        self.body = Circle(self.center, self.body_radius)
        self.body.setFill("white")
        self.body.draw(self.window)

        # Cria o indicador de bateria (círculo verde)
        battery_radius = self.body_radius / 4
        self.battery = Circle(self.center, battery_radius)
        self.battery.setFill(color_rgb(0, 255, 0))
        self.battery.draw(self.window)

    def move(self, dx, dy):
        self.body.move(dx, dy)
        self.battery.move(dx, dy)
        self.center.move(dx, dy)
    
    def move_to_point(self, target_point):
        win_width = int(self.window.getWidth())
        win_height = int(self.window.getHeight())

        min_x = self.body_radius
        max_x = win_width - self.body_radius
        min_y = self.body_radius
        max_y = win_height - self.body_radius

        target_x = max(min_x, min(target_point.getX(), max_x))
        target_y = max(min_y, min(target_point.getY(), max_y))
        
        dx = target_x - self.center.getX()
        dy = target_y - self.center.getY()

        distance = sqrt(dx**2 + dy**2)
        steps = int(distance / 2)
        steps = max(10, steps)

        step_dx = dx / steps
        step_dy = dy / steps

        for _ in range(steps):
            self.move(step_dx, step_dy)
            sleep(0.01)

    
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