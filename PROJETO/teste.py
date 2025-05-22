from graphics import *

class Table:
    def __init__(self, win, id, x1, y1, x2, y2, color="lightgray"):
        self.id = id
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.draw(win)
        label = Text(Point((x1 + x2) / 2, (y1 + y2) / 2), id)
        label.setSize(6)
        label.setTextColor("white")
        label.draw(win)

class Sala:
    def __init__(self):
        self.win = GraphWin("Planta da Sala", 600, 600)
        self.win.setCoords(0, 0, 150, 150)
        self.win.setBackground("white")

    def desenhar_objetos(self, salaxx):
        with open(salaxx, "r") as f:
            for linha in f:
                if linha.strip() == "" or linha.startswith("#"):
                    continue

                partes = linha.strip().split()
                tipo = partes[0]

                if tipo.startswith("M") and len(partes) >= 6:
                    id = tipo
                    x1, y1, x2, y2 = map(float, partes[1:5])
                    color = partes[5] if len(partes) == 6 else "lightgray"
                    Table(self.win, id, x1, y1, x2, y2, color)

                elif tipo == "DIV" and len(partes) == 6:
                    x1, y1, x2, y2 = map(float, partes[1:5])
                    color = partes[5]
                    rect = Rectangle(Point(x1, y1), Point(x2, y2))
                    rect.setFill(color)
                    rect.draw(self.win)

                elif tipo == "PRATOS":
                    x1, y1, x2, y2 = map(float, partes[1:5])
                    rect = Rectangle(Point(x1, y1), Point(x2, y2))
                    rect.setFill("orange")
                    rect.draw(self.win)
                    texto = Text(Point((x1 + x2) / 2, y1 - 3), "Saída Pratos")
                    texto.setTextColor("orange")
                    texto.setSize(6)
                    texto.draw(self.win)

                elif tipo == "ROBOT":
                    x, y = map(float, partes[1:3])
                    circ = Circle(Point(x, y), 5)
                    circ.setFill("red")
                    circ.draw(self.win)
                    texto = Text(Point(x, y + 7), "Robot")
                    texto.setSize(6)
                    texto.draw(self.win)

                elif tipo == "ENTREGA":
                    x, y = map(float, partes[1:3])
                    p = Point(x, y)
                    label = Text(p, "Entrega")
                    label.setTextColor("red")
                    label.setSize(6)
                    label.draw(self.win)

    def esperar(self):
        self.win.getMouse()
        self.win.close()

def main():
    sala = Sala()
    sala.desenhar_objetos("salaxx.txt")
    sala.esperar()

main()
