# gpasort.py
#    A program to sort student information into GPA order.

from gpa1 import Student, makeStudent


def readStudents(filename):
    with open(filename, 'r') as infile:
        students = [makeStudent(line) for line in infile]
    return students


def writeStudents(students, filename):
    # students is a list of Student objects
    with open(filename, 'w') as outfile:
        for s in students:
            print(f"{s.getName()}\t{s.getHours()}\t{s.getQPoints()}",
                  file=outfile)


def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data.sort(key=Student.gpa, reverse=True)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)


if __name__ == '__main__':
    main()
