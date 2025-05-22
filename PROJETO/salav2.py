from graphics import GraphWin, Rectangle, Point, Circle, Text

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
        self.rect.getCenter()
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
        self.win = GraphWin("Projeto", 600, 600)
        self.win.setBackground("white")
        self.win.setCoords(0.0, 0.0, 150, 150)
    
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
                    Table(self.win, x1, y1, x2, y2, cor)
                
                elif tipo == "DIV":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Divisao(self.win, x1, y1, x2, y2, cor)
                
                elif tipo == "B":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Bancada(self.win, x1, y1, x2, y2, cor)

                elif tipo == "E":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    radius = float(partes[3])
                    cor = partes[4]
                    Estacao(self.win, x1, y1, radius, cor)

                elif tipo == "S":  
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Saida(self.win, x1, y1, x2, y2, cor)
                
    def run(self, salaxx):
        self.desenhar(salaxx)
        # Espera por um clique antes de fechar
        ponto = self.win.getMouse()
        if self.Saida.detetar(ponto):
            self.win.close()

def main():
    sala_obj = Sala()
    sala_obj.run("salaxx.txt")
main()
