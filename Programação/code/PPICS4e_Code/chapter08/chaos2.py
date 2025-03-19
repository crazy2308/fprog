# File: chaos2.py
# A simple program illustrating chaotic behavior.

def get_inputs():
    inputs = input("Enter two starting values between 0 and 1: ")
    a, b = inputs.split()
    return float(a), float(b)


def logisticfn(x):
    return 3.9 * x * (1-x)


def formatvalue(x):
    digits = str(round(x, 6))
    return digits.ljust(8)


def main():
    print("This program illustrates a chaotic function")
    x1, x2 = get_inputs()
    print("\ninput:", str(x1).center(8), " ", str(x2).center(8))
    print("---------------------------")
    for _ in range(10):
        x1 = logisticfn(x1)
        x2 = logisticfn(x2)
        print(" "*6, formatvalue(x1), " ", formatvalue(x2))


main()
