# printfile2.py
#    Prints a file to the screen.


def main():
    fname = input("Enter filename: ")
    with open(fname, "r") as infile:
        data = infile.read()
    print(data)


main()
