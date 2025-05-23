from graphics import *

def converter_para_negativo(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getPixel(x, y)
            negativo = color_rgb(255 - r, 255 - g, 255 - b)
            imagem.setPixel(x, y, negativo)
        update()

def main():
    nome_arquivo = input("Digite o nome da imagem (GIF ou PPM): ")
    imagem = Image(Point(0, 0), nome_arquivo)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = GraphWin("Negativo da Imagem", largura, altura)
    imagem.move(largura / 2, altura / 2)
    imagem.draw(janela)

    print("Clique na imagem para converter para o negativo...")
    janela.getMouse()

    converter_para_negativo(imagem)

    nome_saida = input("Escreva o nome para salvar a imagem negativa: ")
    imagem.save(nome_saida)

    print("Imagem guardada como", nome_saida)
    janela.getMouse()
    janela.close()

main()
