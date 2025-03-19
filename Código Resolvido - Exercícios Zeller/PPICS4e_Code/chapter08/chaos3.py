# File: chaos3.py
# A simple program illustrating chaotic behavior.

def get_inputs():
    inputs = input("Enter two starting values between 0 and 1: ")
    a, b = inputs.split()
    return float(a), float(b)


def logisticfn(x):
    return 3.9 * x * (1-x)


def main():
    print("This program illustrates a chaotic function")
    x1, x2 = get_inputs()
    print(f"\ninput: {x1:^8}   {x2:^8}")
    print("---------------------------")
    for _ in range(10):
        x1 = logisticfn(x1)
        x2 = logisticfn(x2)
        print(f"       {x1:8.6f}   {x2:8.6f}")


main()
