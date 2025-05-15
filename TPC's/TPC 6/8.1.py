from graphics import *

class GrupoGrafico:
    def __init__(self, ancora):
        self.ancora = Point(ancora.getX(), ancora.getY())
        self.objetos = []

    def retornaAncora(self):
        return Point(self.ancora.getX(), self.ancora.getY())

    def adicionaObjeto(self, objeto):
        self.objetos.append(objeto)

    def move(self, dx, dy):
        self.ancora.move(dx, dy)
        for obj in self.objetos:
            obj.move(dx, dy)

    def desenha(self, win):
        for obj in self.objetos:
            obj.draw(win)

    def apaga(self):
        for obj in self.objetos:
            obj.undraw()
            
def main():
    win = GraphWin("Grupo Gráfico - Cara movível", 400, 400)

    ancora = Point(200, 200)
    grupo = GrupoGrafico(ancora)

    face = Circle(ancora, 50)
    olho_esq = Circle(Point(180, 190), 5)
    olho_dir = Circle(Point(220, 190), 5)
    boca = Line(Point(185, 215), Point(215, 215))

    grupo.adicionaObjeto(face)
    grupo.adicionaObjeto(olho_esq)
    grupo.adicionaObjeto(olho_dir)
    grupo.adicionaObjeto(boca)

    grupo.desenha(win)

    while True:
        click = win.getMouse()
        novaX = click.getX()
        novaY = click.getY()

        ancora_atual = grupo.retornaAncora()
        dx = novaX - ancora_atual.getX()
        dy = novaY - ancora_atual.getY()

        grupo.move(dx, dy)

main()