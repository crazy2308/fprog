
from graphics import GraphWin, Text, Point, Rectangle

class sala:
   
    def __init__(self):
        self.sala = GraphWin("Projeto", 600, 600)
        self.sala.setBackground("white")
        self.sala.setCoords(0.0, 0.0, 150, 150)
        self.sala.getMouse()
        self.sala.close()

    def desenhar_mesa(self, x1, y1, x2, y2):
        self.mesa = Rectangle(Point(x1, y1), Point(x2, y2))
        self.mesa.setFill(cor)
        self.mesa.draw(self.sala)
        return self.mesa