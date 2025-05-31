#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro cria todas as funções e classes e precisamos para definir o projeto final

from graphics import *
from math import * #Justificar esta biblioteca
from time import sleep #Justificar esta biblioteca

class Waiter:
    def __init__(self, window, center_point, body_radius, battery_level, x_min, y_min, x_max, y_max, posicoes_mesa):
        
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

        self.window = window
        self.center = center_point
        self.body_radius = body_radius
        self.battery_level = battery_level
        self.posicoes_mesa = posicoes_mesa
        self.obstaculos = []  # Lista para armazenar os obstáculos
        self.obstaculos_imagens = []  # Lista para armazenar as imagens dos obstáculos

        # Posição inicial
        self.posicao_x = self.center.getX()
        self.posicao_y = self.center.getY()

        # Lista para armazenar as partes do robô
        self.body_parts = []

        # Corpo do robô
        self.body = Circle(self.center, self.body_radius)
        self.body.setFill("white")
        self.body.draw(self.window)
        self.body_parts.append(self.body)

        # Indicador de bateria
        battery_radius = self.body_radius / 4
        self.battery = Circle(self.center, battery_radius)
        self.battery.setFill(color_rgb(0, 255, 0))
        self.battery.draw(self.window)
        self.body_parts.append(self.battery)

        
    def mover_tier1(self, destino_x, destino_y):
       
        passos = 100
        dx = (destino_x - self.posicao_x) / passos
        dy = (destino_y - self.posicao_y) / passos

        for i in range(passos):
            novo_x = self.posicao_x + dx
            novo_y = self.posicao_y + dy

            for parte in self.body_parts:
                parte.move(dx, dy)

            self.posicao_x = novo_x
            self.posicao_y = novo_y
            time.sleep(0.005)

    def mover_tier2(self, destino_x, destino_y):       

        passos = 100
        dx = (destino_x - self.posicao_x) / passos
        dy = (destino_y - self.posicao_y) / passos

        for i in range(passos):

            novo_x = self.posicao_x + dx
            novo_y = self.posicao_y + dy

        # Verifica se houve clique durante o movimento
            click = self.window.checkMouse()
            if click:
                print("Clique durante o movimento!")
                self.obstaculo(click)  # Adiciona obstáculo

            colisao, posicao = self.colisao(novo_x, novo_y)

            if colisao == "bateu":
                print(f"Colisão detectada com obstáculo na posição {posicao}!")
                time.sleep(2.0)
                self.obstaculos.pop(posicao)
                self.obstaculos_imagens[posicao].undraw()
                self.obstaculos_imagens.pop(posicao)  # ← REMOVE a imagem da lista também!


            for parte in self.body_parts:
                parte.move(dx, dy)

            self.posicao_x = novo_x
            self.posicao_y = novo_y
            time.sleep(0.005)

    def table_check(self, click_point, mesas):

        for mesa in mesas:
            if mesa.det_table(click_point):  # Verifica se o clique está dentro da mesa
                print("Clique detectado em uma mesa!")
                self.check_table() # Chama a função para verificar a mesa
                return True  # Indica que o clique foi em uma mesa
        return False  # Indica que o clique não foi em uma mesa
    
    def go_to_table_tier1(self, mesas):
        ponto1 = Point(97.0, 135.0)  # Docking station
        ponto2 = Point(97.0, 145.0)  # Ponto de destino do robô
        ponto_intermedio = Point(75, 136)  # Ponto de transição

        # Desenha a imagem em todas as mesas e guarda as referências
        imagens = []
        for mesa in mesas:
            center = mesa.rect.getCenter()
            img = Image(center, 'bifana.png')
            img.draw(self.window)
            imagens.append((mesa, img))

        # Para cada mesa, segue o percurso restrito, espera, retira a imagem, vai ao ponto intermédio, espera, segue para a próxima
        for mesa, img in imagens:
            center = mesa.rect.getCenter()
            if mesa.ident == "EE":
                self.mover_tier1(center.getX() - 15, 135.0)
                self.mover_tier1(center.getX() - 15, center.getY())
                self.mover_tier1(center.getX() - 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(center.getX() - 15, center.getY())
                self.mover_tier1(center.getX() - 15, 135.0)
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            elif mesa.ident == "EC":
                self.mover_tier1(center.getX() + 15, 135.0)
                self.mover_tier1(center.getX() + 15, center.getY())
                self.mover_tier1(center.getX() + 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            elif mesa.ident == "DC":
                self.mover_tier1(center.getX() - 15, 135.0)
                self.mover_tier1(center.getX() - 15, center.getY())
                self.mover_tier1(center.getX() - 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            elif mesa.ident == "DD":
                self.mover_tier1(center.getX() + 15, 135.0)
                self.mover_tier1(center.getX() + 15, center.getY())
                self.mover_tier1(center.getX() + 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(center.getX() + 15, center.getY())
                self.mover_tier1(self.posicao_x, 135.0)
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            else:
                # Caso não seja nenhum dos identificadores acima, faz um movimento simples
                self.mover_tier1(center.getX(), center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(ponto_intermedio.getX(), ponto_intermedio.getY())
                sleep(1.0)

        # No fim, volta à docking station
        self.mover_tier1(ponto1.getX(), ponto1.getY())
        self.mover_tier1(ponto2.getX(), ponto2.getY())

    def go_to_table_tier2(self, click_point, mesas):
        ponto1 = Point(97.0, 135.0)  # Ponto inicial do robô
        ponto2 = Point(75.0, 136.0)  # Ponto de destino do robô
        ponto3 = Point(97.0, 145.0)  # Ponto de destino do robô
        self.running = True  # Garante que o robô está ativo
        
        for mesa in mesas:
            if mesa.det_table(click_point):  # Verifica se o clique está dentro da mesa
                mesa.rect.setFill("green")  # Muda a cor da mesa para verde
                print("Clique detectado em uma mesa!")
                # Obtém o centro da mesa
                center = mesa.rect.getCenter()
                img = Image(center, 'bifana.png')
                    
                self.mover_tier2(ponto1.getX(), ponto1.getY())  # Move o robô para o ponto inicial
                
                if mesa.ident in ["EE"]:
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(self.posicao_x, 135.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                if mesa.ident in ["EC"]:
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                if mesa.ident in ["DC"]:
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                if mesa.ident in ["DD"]:
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(self.posicao_x, 135.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                mesa.rect.setFill(mesa.cor_original)
            
                return True  # Indica que o clique foi em uma mesa
                    
 
        return False  # Indica que o clique não foi em uma mesa
    
    def colisao(self, novo_x, novo_y):

        for i, (x1, x2, y1, y2) in enumerate(self.obstaculos):
            if x1 <= novo_x <= x2 and y1 <= novo_y <= y2:
                print("Colisão detectada com um obstáculo!")
                return "bateu", i  
        return 0, 0
        

    def obstaculo(self, click_point):

        x = click_point.getX()
        y = click_point.getY()
            
        print("Clique detectado fora das mesas!")
        cerveja = Image(Point(x, y), "jola.png")
        cerveja.draw(self.window)

        x1 = x - 10
        x2 = x + 10
        y1 = y - 8
        y2 = y + 8
         # Evita colocar obstáculo sobre o botão SAIR
        self.obstaculos.append((x1,x2,y1,y2))  # Adiciona a cerveja à lista de obstáculos
        self.obstaculos_imagens.append(cerveja)  # Adiciona a imagem da cerveja à lista de imagens

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
    def __init__(self, win, x1, y1, x2, y2, color, ident):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)
        self.ident = ident
        self.cor_original = color

    def det_table(self, point):

        x = point.getX()
        y = point.getY()
        x1 = self.rect.getP1().getX()
        y1 = self.rect.getP1().getY()
        x2 = self.rect.getP2().getX()
        y2 = self.rect.getP2().getY()

        return x1 <= x <= x2 and y1 <= y <= y2

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
    def __init__(self, win, x1, y1, x2, y2):
        self.win = win
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.draw(win)
        
         # Cria botão
        self.button, self.label = Button.create_button(win, Point(x1, y1), Point(x2, y2), "SAIR")
        
        # Cria imagem sobre o botão
        centro = self.rect.getCenter()
        Image(centro, "sair2.png").draw(self.win)
        

class Sala:
    def __init__(self):
        self.win2 = GraphWin("Zé das Bifanas", 600, 600)
        self.x1 = 0.0
        self.x2 = 150
        self.y1 = 0
        self.y2 = 150
        self.win2.setCoords(self.x1, self.y1, self.x2, self.y2)
        self.fundo = Image(Point(75, 75), "chao_madeira_v3.gif")
        self.fundo.draw(self.win2)
        self.saida = None
        self.mesas = []  # Lista para armazenar as mesas
        self.posicoes_mesa = []  # Lista para armazenar as posições das mesas

    def desenhar(self, sala49):
        arquivo = open("sala49.txt", "r")
        with arquivo as dados:
            for linha in dados:
                if linha.strip() == "" or linha.startswith("#"):  # Ignorar linhas vazias ou comentários
                    continue
                partes = linha.strip().split()
                tipo = partes[0]

                if tipo.startswith("M"):  # Mesas
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    ident = partes[6] # Identificador opcional
                    mesa = Table(self.win2, x1, y1, x2, y2, cor, ident)
                    
                    self.posicoes_mesa.append((x1, y1, x2, y2))
                    self.mesas.append(mesa)  # Adiciona a mesa à lista
                
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
                    self.saida = Saida(self.win2, x1, y1, x2, y2)  # Guarda referência
    
    def run(self, sala49):
        self.desenhar(sala49)

    def devolver_mesas(self):
        return self.posicoes_mesa