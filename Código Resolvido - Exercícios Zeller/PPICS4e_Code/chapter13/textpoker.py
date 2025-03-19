# textpoker.py


class TextInterface:

    def __init__(self):
        print("Welcome to video poker.")

    def setMoney(self, amt):
        print(f"You currently have ${amt}.")

    def setDice(self, values):
        print("Dice:", values)

    def wantToPlay(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in ["y", "Y"]

    def close(self):
        print("\nThanks for playing!")

    def showResult(self, msg, score):
        print(f"{msg}. You win ${score}.")

    def chooseDice(self):
        instr = input("Enter which dice to roll (<Enter> to stop): ")
        indexes = [int(x) for x in instr.split()]
        return indexes


if __name__ == "__main__":
    from pokerapp import PokerApp
    inter = TextInterface()
    app = PokerApp(inter)
    app.run()
