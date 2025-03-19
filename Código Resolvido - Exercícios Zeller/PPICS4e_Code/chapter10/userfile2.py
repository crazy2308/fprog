# userfile2.py
#    Program to create a file of usernames in batch mode.

#    This version creates a backup file before overwriting
#    an existing usernames file

from pathlib import Path


def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get the file names
    inPath = Path(input("What file are the names in? "))
    outPath = Path(input("What file should the usernames go in? "))
    if outPath.exists():
        backupPath = outPath.with_suffix(".bak")
        print(f"Renaming existing file {outPath.name} to {backupPath.name}")
        outPath.rename(backupPath)

    # open the files
    with inPath.open("r") as infile, outPath.open("w") as outfile:
        # process each line of the input file
        for line in infile:
            # get the first and last names from line
            first, last = line.split()
            # create the username
            uname = (first[0]+last[:7]).lower()
            # write it to the output file
            print(uname, file=outfile)

    print("Usernames have been written to", outPath)


if __name__ == "__main__":
    main()

