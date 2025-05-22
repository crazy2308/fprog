from graphics import *

def converter_para_cinza(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    for y in range(altura):
        for x in range(largura):
            cor = imagem.getPixel(x, y)
            r, g, b = cor  
            brilho = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            cinza = color_rgb(brilho, brilho, brilho)
            imagem.setPixel(x, y, cinza)
        update()

def main():
    nome_arquivo = input("Digite o nome da imagem (GIF ou PPM): ")
    imagem = Image(Point(0, 0), nome_arquivo)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = GraphWin("Conversor para tons de cinza", largura, altura)
    imagem.move(largura / 2, altura / 2)
    imagem.draw(janela)

    print("Clique na imagem para converter para tons de cinza...")
    janela.getMouse()

    converter_para_cinza(imagem)

    nome_saida = input("Escreva o nome para salvar a imagem em tons de cinza: ")
    imagem.save(nome_saida)

    print("Imagem guardada como", nome_saida)
    janela.getMouse()
    janela.close()

main()
