from graphics import * # type: ignore #


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

    message.setText("Clica para sair.") 
    win.getMouse()


main()
