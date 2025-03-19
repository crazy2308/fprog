# textpokerapp.py -- video dice poker using a text-based interface.

from pokerapp import PokerApp
from textpoker import TextInterface

inter = TextInterface()
app = PokerApp(inter)
app.run()
