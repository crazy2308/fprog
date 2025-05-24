#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro cria todas as funções e classes e precisamos para definir o projeto final

from graphics import *
from math import * #Justificar esta biblioteca
from time import * #Justificar esta biblioteca

class Waiter:
    def __init__(self, window, center_point, body_radius, battery_level, x_min, y_min, x_max, y_max):
        self.window = window
        self.center = center_point
        self.body_radius = body_radius
        self.battery_level = battery_level
        self.ignore_collisions = False  # Só ignora colisões quando ativado

        # Guardar limites
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

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
        min_x = self.x_min + self.body_radius
        max_x = self.x_max - self.body_radius
        min_y = self.y_min + self.body_radius
        max_y = self.y_max - self.body_radius

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
            new_x = self.center.getX() + step_dx
            new_y = self.center.getY() + step_dy
            if min_x <= new_x <= max_x and min_y <= new_y <= max_y:
                self.move(step_dx, step_dy)
                sleep(0.01)
            else:
                break
    
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
    
class Table:
    def __init__(self, win, x1, y1, x2, y2, color):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)

class Divisao:
    def __init__(self, win, x1, y1, x2, y2, color):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)


class Bancada:
    def __init__(self, win, x1, y1, x2, y2, color):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)

class Estacao:
    def __init__(self, win, x1, y1, radius, color):
        self.circ = Circle(Point(x1, y1), radius)
        self.circ.setFill(color)
        self.circ.setOutline("black")
        self.circ.draw(win)

class Saida:
    def __init__(self, win, x1, y1, x2, y2, color):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("red4")
        self.rect.draw(win)
        centro = self.rect.getCenter()
        texto = Text(centro, "Saída")
        texto.setSize(10)
        texto.setTextColor("black")
        texto.draw(win)
     
    def detetar(self, ponto):
        x = ponto.getX()
        y = ponto.getY()
        return ((132 <= x <= 150) and (0 <= y <= 10))

class Sala:
    def __init__(self):
        self.win2 = GraphWin("Zé das Bifanas", 600, 600)
        self.win2.setCoords(0.0, 0.0, 150, 150)
        self.fundo = Image(Point(75, 75), "chao_madeira_v3.gif")
        self.fundo.draw(self.win2)
        self.saida = None

    def desenhar(self, salaxx):
        arquivo = open("salaxx.txt", "r")
        with arquivo as dados:
            for linha in dados:
                if linha.strip() == "" or linha.startswith("#"): #caso não haja nada na linha ou um comentario
                    continue
                partes = linha.strip().split()
                tipo = partes[0]

                if tipo.startswith("M"):
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Table(self.win2, x1, y1, x2, y2, cor)
                
                elif tipo == "DIV":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Divisao(self.win2, x1, y1, x2, y2, cor)
                
                elif tipo == "B":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Bancada(self.win2, x1, y1, x2, y2, cor)

                elif tipo == "E":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    radius = float(partes[3])
                    cor = partes[4]
                    Estacao(self.win2, x1, y1, radius, cor)

                elif tipo == "S":  
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Saida(self.win2, x1, y1, x2, y2, cor)
    
    def run(self, salaxx):
        self.desenhar(salaxx)