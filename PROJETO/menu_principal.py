#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)
#Falta adicionar o jogo em si

from graphics import *
from classes import *
class menu_principal:

    def __init__(self):
        self.win = GraphWin("Zé das Bifanas", 1600, 900, autoflush=True)
        self.win.setCoords(0, 900, 1600, 0)
        self.estado_menu = "main"  #Define a janela como o estado main do menu
        self.show_main_menu()

    def show_main_menu(self):
        self.estado_menu = "main"
        self.background_main = Image(Point(800, 450), "menu_principal.png").draw(self.win) #Cria a imagem de fundo do menu principal

        #Define as coordenadas e os nomes dos botões clicáveis no menu principal
        self.buttons_main = []
        button_main_data = [
            [(290, 670), (510, 800), "TIER1"],
            [(690, 670), (910, 800), "TIER2"],
            [(1090, 670), (1310, 800), "TIER3"],
            [(1405, 40), (1495, 140), "SAIR"],
            [(40, 100), (260, 140), "PROPRIETÁRIOS"]
        ]

        #Cria todos os botões
        for data in button_main_data:
            button, label = Button.create_button(self.win, Point(*data[0]), Point(*data[1]), data[2])
            self.buttons_main.append((button, label))

        #Define todas as imagens dos botões do menu principal
        self.images_main = [
            Image(Point(150, 120), 'botao_proprietarios.png').draw(self.win),
            Image(Point(400, 735), "tier1.png").draw(self.win),
            Image(Point(800, 735), "tier2.png").draw(self.win),
            Image(Point(1200, 735), "tier3.png").draw(self.win),
            Image(Point(1450, 90), "sair.png").draw(self.win)
        ]

    #Remove todas as imagens e desenhos do menu principal, para poder ir para outro menu, o dos autores
    def clear_main_menu(self):
        self.background_main.undraw()
        for button, label in self.buttons_main:
            button.undraw()
            label.undraw()
        for image in self.images_main:
            image.undraw()
    
    #Define o menu dos autores
    def show_authors_menu(self):
        self.estado_menu = "authors"
        self.authors_bg = Image(Point(800, 450), "proprietarios_bg.png").draw(self.win) #Desenha o fundo

        #Define os botões deste menu
        self.authors_buttons = []
        back, label = Button.create_button(self.win, Point(80, 675), Point(170, 775), "VOLTAR") #Cria o botão voltar
        self.authors_buttons.append((back, label))

        #Define as imagens deste menu
        self.images_authors = [
            Image(Point(800, 100), 'nome_proprietarios.png').draw(self.win),
            Image(Point(125, 725), "voltar.png").draw(self.win),
            Image(Point(800, 500), "proprietarios.png").draw(self.win)
        ]

    #Limpa o menu dos autores para poder voltar ao menu principal
    def clear_authors_menu(self):
        self.authors_bg.undraw()
        for image in self.images_authors:
            image.undraw()
        for button, label in self.authors_buttons:
            button.undraw()
            label.undraw()

    def run(self):
        while True:
            click_point = self.win.getMouse() 

            if self.estado_menu == "main":
                for button, label in self.buttons_main:
                    if Button.is_click_in_button(click_point, button):
                        texto = label.getText()
                        if texto == "TIER1":     #Se clicar no botão com o rótulo TIER1 ele importa do projeto.py a função tier1 e executa-a
                            self.win.close()
                            from projeto import tier1
                            tier1()
                            return
                        elif texto == "TIER2":   #Se clicar no botão com o rótulo TIER2 ele importa do projeto.py a função tier2 e executa-a
                            self.win.close()
                            from projeto import tier2
                            tier2()
                            return
                        elif texto == "TIER3":   #Se clicar no botão com o rótulo TIER3 ele importa do projeto.py a função tier3 e executa-a
                            self.win.close()
                            from projeto import tier3 
                            tier3()
                            return
                        elif texto == "SAIR":    #Se clicar no botão sair ele fecha o programa
                            self.win.close()
                            return
                        elif texto == "PROPRIETÁRIOS":   #Se clicar no botão proprietário ele vai para o menu dos autores/créditos
                            self.clear_main_menu()
                            self.show_authors_menu()
                        break

            elif self.estado_menu == "authors":
                for button, label in self.authors_buttons:
                    if Button.is_click_in_button(click_point, button):
                        if label.getText() == "VOLTAR":                 #Se clicar no botão voltar dentro do menu autores ele limpa o menu e volta a desenhar o menu principal
                            self.clear_authors_menu()
                            self.show_main_menu()
                        break


if __name__ == "__main__":     #Apenas executa o programa se estiver a ser executado como código principal. Evitando que corra quando importado.
    game = menu_principal()
    game.run()
