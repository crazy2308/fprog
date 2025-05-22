from graphics import *

def media(valores):
    return sum(valores) / len(valores)

def desenhar_linha_regressao(janela, pontos, largura, altura):
    n = len(pontos)
    x_vals = [p.getX() for p in pontos]
    y_vals = [p.getY() for p in pontos]

    x_media = media(x_vals)
    y_media = media(y_vals)

    soma_x = sum(x_vals)
    soma_y = sum(y_vals)
    soma_xy = sum(x * y for x, y in zip(x_vals, y_vals))
    soma_x2 = sum(x ** 2 for x in x_vals)

    m = (soma_xy - n * x_media * y_media) / (soma_x2 - n * x_media ** 2)

    def regressao_y(x):
        return y_media + m * (x - x_media)

    x1, x2 = 0, largura
    y1, y2 = regressao_y(x1), regressao_y(x2)
    linha = Line(Point(x1, y1), Point(x2, y2))
    linha.setOutline("red")
    linha.setWidth(2)
    linha.draw(janela)

def main():
    largura, altura = 600, 400
    janela = GraphWin("Linha de Regressão", largura, altura)
    janela.setCoords(0, 0, largura, altura)

    botao = Rectangle(Point(10, 10), Point(100, 40))
    botao.setFill("lightgray")
    botao.draw(janela)
    texto_botao = Text(Point(55, 25), "Concluído")
    texto_botao.draw(janela)

    pontos = []
    while True:
        clique = janela.getMouse()
        x, y = clique.getX(), clique.getY()

        if 10 <= x <= 100 and 10 <= y <= 40:
            break

        c = Circle(clique, 3)
        c.setFill("blue")
        c.draw(janela)
        pontos.append(clique)

    if len(pontos) >= 2:
        desenhar_linha_regressao(janela, pontos, largura, altura)

    janela.getMouse()
    janela.close()

main()
