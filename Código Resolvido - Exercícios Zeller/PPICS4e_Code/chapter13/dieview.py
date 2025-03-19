# dieview.py

from graphics import *


class DieView:
    """DieView is a widget that displays a graphical representation of a
    standard six-sided die.
    """

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.: d1 = GDie(myWin, Point(40,50), 20)
           creates a die centered at (40,50) having sides of length
           20.
        """

        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size    # radius of each pip
        hsize = size / 2.0         # half of size
        offset = 0.6 * hsize       # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create a list of 7 circles in standard pip locations
        self.pips = []
        self._addPip(cx-offset, cy-offset),  # upper left
        self._addPip(cx-offset, cy),         # left center
        self._addPip(cx-offset, cy+offset),  # lower left
        self._addPip(cx, cy),                # center
        self._addPip(cx+offset, cy-offset),  # upper right
        self._addPip(cx+offset, cy),         # center right
        self._addPip(cx+offset, cy+offset)   # lower right

        # Create a table saying which pips are on for each value.
        self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6],
                        [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

        # start with view showing 1
        self.setValue(1)

    def _addPip(self, x, y):
        """Internal helper method to add a pip at (x,y)"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        self.pips.append(pip)

    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips on
        onlist = self.onTable[value]
        for i in onlist:
            self.pips[i].setFill(self.foreground)
