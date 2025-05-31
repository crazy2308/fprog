from graphics import *
import random

# Função para desenhar os botões
def draw_buttons(win):
    buttons = []
    labels = ["Porta 1", "Porta 2", "Porta 3"]
    for i in range(3):
        rect = Rectangle(Point(50 + i*120, 100), Point(150 + i*120, 200))
        rect.setFill("lightgray")
        rect.draw(win)
        text = Text(rect.getCenter(), labels[i])
        text.draw(win)
        buttons.append((rect, labels[i]))
    return buttons

# Função para desenhar o botão "Quit"
def draw_quit_button(win):
    rect = Rectangle(Point(200, 250), Point(300, 300))
    rect.setFill("red")
    rect.draw(win)
    text = Text(rect.getCenter(), "Quit")
    text.setTextColor("white")
    text.draw(win)
    return rect

# Função para exibir mensagens
def show_message(win, message):
    msg = Text(Point(250, 50), message)
    msg.setSize(12)
    msg.draw(win)
    return msg

# Verifica se um clique foi dentro de um botão
def button_clicked(click, button):
    p1 = button.getP1()
    p2 = button.getP2()
    return p1.getX() <= click.getX() <= p2.getX() and p1.getY() <= click.getY() <= p2.getY()

def main():
    win = GraphWin("Jogo das portas", 500, 350)
    win.setBackground("white")

    wins = 0
    losses = 0

    buttons = draw_buttons(win)
    quit_button = draw_quit_button(win)

    stats_text = Text(Point(250, 20), f"Vitórias: {wins}  Derrotas: {losses}")
    stats_text.draw(win)

    while True:
        special = random.randint(0, 2)
        click = win.getMouse()

        if button_clicked(click, quit_button):
            break

        for i, (rect, label) in enumerate(buttons):
            if button_clicked(click, rect):
                if i == special:
                    msg = show_message(win, "Ganhaste!")
                    wins += 1
                else:
                    msg = show_message(win, f"Perdeste, era a porta {buttons[special][1]}")
                    losses += 1
                stats_text.setText(f"Vitórias: {wins}  Derrotas: {losses}")
                win.getMouse()  # Espera para o jogador ver o resultado
                msg.undraw()
                break

    win.close()

main()