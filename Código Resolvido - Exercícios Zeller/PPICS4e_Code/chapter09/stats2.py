# stats2.py
#   A more pythonic version of a simple statistics library.

from math import sqrt


def getNumbers():
    instr = input("Enter numbers below separated by spaces and press <Enter>:\n")
    nums = [float(numstr) for numstr in instr.split()]
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


def outliers(nums, xbar, s):
    return [x for x in nums if abs((x-xbar)/s) > 3]


def main():
    print("This program computes mean, median and standard deviation.")

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)


if __name__ == '__main__':
    main()
