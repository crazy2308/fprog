# roller2.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView.

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import DieView


class Roller:

    def __init__(self):

        # create the application window
        self.win = GraphWin("Dice Roller")
        self.win.setCoords(0, 0, 10, 10)
        self.win.setBackground("green2")

        # Draw the interface widgets
        self.die1 = DieView(self.win, Point(3, 7), 2)
        self.die2 = DieView(self.win, Point(7, 7), 2)
        self.rollButton = Button(self.win, Point(5, 4.5), 6, 1, "Roll Dice")
        self.rollButton.activate()
        self.quitButton = Button(self.win, Point(5, 1), 2, 1, "Quit")

    def run(self):
        pt = self.win.getMouse()
        while not self.quitButton.clicked(pt):
            if self.rollButton.clicked(pt):
                value1 = randrange(1, 7)
                self.die1.setValue(value1)
                value2 = randrange(1, 7)
                self.die2.setValue(value2)
                self.quitButton.activate()
            pt = self.win.getMouse()
        self.win.close()


if __name__ == "__main__":
    app = Roller()
    app.run()
