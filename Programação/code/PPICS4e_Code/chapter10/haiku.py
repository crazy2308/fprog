# haiku.py

def main():
    haiku = ["White space and syntax",
             "Python code flows like water",
             "Solutions emerge"]

    print("I have a haiku for you.")
    fname = input("Enter a file name to receive the haiku: ")
    with open(fname, "w") as haikufile:
        for line in haiku:
            print(line, file=haikufile)

    print(f"Look in {fname} to see your haiku")


main()
