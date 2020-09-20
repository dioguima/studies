#!/bin/python3

import math
import os
import random
import re
import sys

def getSumHourglass(x_center, y_center, arr):
    return (arr[y_center][x_center] + 
        arr[y_center - 1][x_center] + arr[y_center - 1][x_center - 1] + arr[y_center - 1][x_center + 1] + 
        arr[y_center + 1][x_center] + arr[y_center + 1][x_center - 1] + arr[y_center + 1][x_center + 1]);



# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for y in range(1, len(arr) - 1):
        for x in range(1, len(arr[y]) - 1):
            sums.insert(0, getSumHourglass(x, y, arr))
    sums.sort()
    return sums[-1]

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result) + '\n')
