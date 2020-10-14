#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    new_array = [None] * len(a)
    for index in range(len(a)):
        index_to_search = index + d
        if(index_to_search >= len(a)):
            index_to_search -= len(a)
        new_array[index] = a[index_to_search]
    return new_array

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))