# addinterest3.py

from graphics import Text, Point


def addInterest(balance, rate):
    newBalance = float(balance.getText()) * (1+rate)
    balance.setText(str(newBalance))


def test():
    amount = Text(Point(0, 0), "1000")
    rate = 0.05
    addInterest(amount, rate)
    print(amount.getText())


test()
