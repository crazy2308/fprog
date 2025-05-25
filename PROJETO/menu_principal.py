#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)
#Falta adicionar o jogo em si

from graphics import *
from classes import *

class menu_principal:

    def __init__(self):
        self.win = GraphWin("Zé das Bifanas", 1600, 900, autoflush=True)
        self.win.setCoords(0, 900, 1600, 0)
        self.estado_menu = "main"  # estado inicial
        self.show_main_menu()

    def show_main_menu(self):
        self.estado_menu = "main"
        self.background_main = Image(Point(800, 450), "menu_principal.png").draw(self.win)

        self.buttons_main = []
        button_main_data = [
            [(690, 670), (910, 800), "COMEÇAR"],
            [(1405, 40), (1495, 140), "SAIR"],
            [(40, 100), (260, 140), "PROPRIETÁRIOS"]
        ]
        for data in button_main_data:
            button, label = Button.create_button(self.win, Point(*data[0]), Point(*data[1]), data[2])
            self.buttons_main.append((button, label))

        self.images_main = [
            Image(Point(150, 120), 'botao_proprietarios.png').draw(self.win),
            Image(Point(800, 735), "comecar.png").draw(self.win),
            Image(Point(1450, 90), "sair.png").draw(self.win)
        ]

    def clear_main_menu(self):
        self.background_main.undraw()
        for button, label in self.buttons_main:
            button.undraw()
            label.undraw()
        for image in self.images_main:
            image.undraw()

    def show_authors_menu(self):
        self.estado_menu = "authors"
        self.authors_bg = Image(Point(800, 450), "proprietarios_bg.png").draw(self.win)

        self.authors_buttons = []
        back, label = Button.create_button(self.win, Point(80, 675), Point(170, 775), "VOLTAR")
        self.authors_buttons.append((back, label))

        self.images_authors = [
            Image(Point(800, 100), 'nome_proprietarios.png').draw(self.win),
            Image(Point(125, 725), "voltar.png").draw(self.win),
            Image(Point(800, 500), "proprietarios.png").draw(self.win)
        ]

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
                        if texto == "COMEÇAR":
                            self.win.close()
                            from projeto import tier1  # <-- Importa aqui!
                            tier1()
                            return
                        elif texto == "SAIR":
                            self.win.close()
                            return
                        elif texto == "PROPRIETÁRIOS":
                            self.clear_main_menu()
                            self.show_authors_menu()
                        break

            elif self.estado_menu == "authors":
                for button, label in self.authors_buttons:
                    if Button.is_click_in_button(click_point, button):
                        if label.getText() == "VOLTAR":
                            self.clear_authors_menu()
                            self.show_main_menu()
                        break


if __name__ == "__main__":
    game = menu_principal()
    game.run()
