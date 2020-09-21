#!/bin/python3

import math
import os
import random
import re
import sys

def findIndexNumber(number, arr):
    for i in range(number - 1, len(arr)):
        if arr[i] == number:
            return i
    return -1

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    i = 0
    swaps = 0
    while i < len(arr):
        current_number = arr[i]
        if current_number != i + 1:
            aux_var = arr[current_number - 1]
            arr[current_number - 1] = arr[i]
            arr[i] = aux_var
            swaps += 1
        else:
            i += 1
    return swaps

if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res) + '\n')

