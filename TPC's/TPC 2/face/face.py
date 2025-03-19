from time import time
from graphics import * # type: ignore #


def main():
    win = GraphWin("Mas que cara fixe!", 539, 360)  # type: ignore
    #win.setBackground(color_rgb(0, 0, 0))
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    
    cara = Image(Point(5,5), "cara.gif")
    cara.draw(win)

    nariz = Image(Point(4.888475836431227,6.016713091922005), "nose.gif")
    nariz.draw(win)

    olho1 = Image(Point(4.4237918215613385,6.740947075208913), "olho.gif")
    olho1.draw(win)

    olho2 = Image(Point(5.33457249070632,6.740947075208913), "olho.gif")
    olho2.draw(win)

    boca = Image(Point(4.907063197026022,4.986072423398329), "boca.gif")
    boca.draw(win)
    
    fundo = Rectangle(Point(3, 0.2), Point(7, 0.8))  # Ajuste os valores conforme necessário
    fundo.setFill("white")  # Cor de fundo
    fundo.setOutline("black")  # Sem contorno visível
    fundo.draw(win) 
    message = Text(Point(5, 0.5), "Olha é o Zé")  # type: ignore
    message.draw(win)
    
    time.sleep(3)
    message.setText("Clica para sair.") 
    win.getMouse()


main()