from graphics import *  # type: ignore


def main():
    win = GraphWin("Desenha um Retângulo", 500, 500)  # type: ignore
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Clica nos cantos do retângulo")  # type: ignore
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    retangulo = Rectangle(p1, p2)  # type: ignore
    retangulo.setFill("darkslategrey")
    retangulo.setOutline("red")
    retangulo.draw(win)

    largura = abs(p2.getX() - p1.getX())

    altura = abs(p2.getY() - p1.getY())

    perimetro = 2 * (largura + altura)

    area = largura * altura

    texto_resultado = "Perímetro: " + str(perimetro) + ", Área: " + str(area)
    resultado_texto = Text(Point(5, 1), texto_resultado)
    resultado_texto.setSize(10)
    resultado_texto.draw(win)

    message.setText("Clica para sair.")
    win.getMouse()
    win.close()


main()
