# stats3.py
#   Satistics library with file operations added.

from math import sqrt
from pathlib import Path
import pickle
from urllib.request import urlopen


def getNumbers():
    nums = []     # start with an empty list

    instr = input("Enter numbers separated by spaces and press <Enter>:\n")
    nums = [float(numstr) for numstr in instr.split()]
    return nums


def getNumbersFromFile1(fname):
    # Simple version that works with exactly 1 number per line
    with open(fname, "r") as infile:
        nums = [float(line) for line in infile]
    return nums


def getNumbersFromFile(fname):
    # Robust version that allows multiple numbers per line
    #   and tolerates blank lines
    nums = []
    with open(fname, "r") as infile:
        for line in infile:
            newnums = [float(x) for x in line.split()]
            nums.extend(newnums)
    return nums


def getNumbersFromFiles(basedir, pattern):
    # Get all numbers from a set of files using globbing
    path = Path(basedir)
    nums = []
    for filepath in path.glob(pattern):
        newnums = getNumbersFromFile(filepath)
        nums.extend(newnums)
    return nums


def storeData(nums, path):
    # pickle the list of nums to a file
    with open(path, "wb") as outfile:
        pickle.dump(nums, outfile)


def loadData(path):
    # restore pickled list
    with open(path, "rb") as infile:
        nums = pickle.load(infile)
    return nums


def getNumbersFromURL(url):
    nums = []
    with urlopen(url) as infile:
        for line in infile:
            line = line.decode()
            newnums = [float(x) for x in line.split()]
            nums.extend(newnums)
    return nums


def mean(nums):
    return sum(nums) / len(nums)


def stdDev(nums, xbar):
    squared_devs = [(num-xbar)**2 for num in nums]
    return sqrt(sum(squared_devs)/(len(nums)-1))


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos-1]) / 2.0
    else:
        med = nums[midPos]
    return med


def outliers(nums):
    xbar = mean(nums)
    s = stdDev(nums, xbar)
    return [x for x in nums if abs((x-xbar)/s) > 3]


def main():
    print("This program computes mean, median and standard deviation")
    print("of the numbers in a file.")

    fname = input("Enter the name of the file to process: ")
    data = getNumbersFromFile(fname)
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)
  
    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)


if __name__ == '__main__':
    main()
