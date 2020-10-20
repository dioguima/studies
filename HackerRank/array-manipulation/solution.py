#!/bin/python3

import math
import os
import random
import re
import sys

def arrayManipulationBruteForce(n, queries):
    
    array = [0 for i in range(n)]

    for query in queries:
        for i in range(query[0] - 1,query[1]):
            array[i] += query[2]
    
    return max(array)

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    array = [0 for i in range(n)]

    for query in queries:
        array[query[0] - 1] += query[2]
        if query[1] < n:
            array[query[1]] -= query[2]

    max_value = array[0]
    current_value = array[0]
    for i in range(1, n):
        if current_value + array[i] != current_value:
            current_value = current_value + array[i]
            if current_value > max_value:
                max_value = current_value
    return max_value

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
