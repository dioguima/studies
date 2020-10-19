#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    inclusive = arr[0]
    exclusive = 0

    for i in range(1, len(arr)):
        aux = inclusive
        inclusive = max(arr[i], arr[i] + exclusive, inclusive)
        exclusive = aux
    
    return max(inclusive, exclusive)
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(str(res) + '\n')
