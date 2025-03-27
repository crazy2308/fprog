from graphics import *
import time

def window(): #Definir o tamanha da janela por input do utilizador

    largura = int(input("Largura da janela: "))
    altura = int(input("Altura da janela: "))

    win = GraphWin("Círculo", largura, altura)
    win.setCoords(0, 0, 100, 100)
    
    return win

def definirraio():
    return int(input("Raio do círculo: "))

def defenircoordenadas():

    x = int(input("X inicial: "))
    y = int(input("Y inicial: "))

    return x, y

def defenircirculo(win, x, y, raio):
    circulo = Circle(Point(x, y), raio)
    circulo.setFill ("Red")
    circulo.draw(win)

    return circulo

def move(win, raio, circulo):
    
    dx, dy = 1, 1

    while True:
        time.sleep(0.02)

        circulo.move(dx, dy)
        centro = circulo.getCenter()

        x, y = centro.getX(), centro.getY()

        if x - raio <= 0 or x + raio >= 100:
            dx = -dx
        if y - raio <= 0 or y + raio >= 100:
            dy = -dy
        if win.checkMouse(): 
            break

def main():
    print("Bem-vindo ao loop do dvd.")
    time.sleep(1.5)
    input("Pressione Enter para continuar...")

    raio = definirraio()
    win = window()
    x, y = defenircoordenadas()
    circulo = defenircirculo(win, x, y, raio)

    move(win, raio, circulo)

    win.getMouse()
    win.close()

main()