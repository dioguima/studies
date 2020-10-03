#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the commonChild function below.
# def commonChild(s1, s2):
#     result = None
#     if len(s1) == 0 or len(s2) == 0:
#         result = 0
#     elif s1[-1] == s2[-1]:
#         result = 1 + commonChild(s1[:-1], s2[:-1])
#     else:
#         result = max(commonChild(s1[:-1], s2), commonChild(s1, s2[:-1]))
#     return result

def commonChild(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    matrix = [[0 for j in range(len_s2 + 1)] for i in range(len_s1 + 1)]
    
    for i1 in range(len_s1):
        for i2 in range(len_s2):
            if s1[i1] == s2[i2]:
                matrix[i1 + 1][i2 + 1] = 1 + matrix[i1][i2]
            else:
                matrix[i1 + 1][i2 + 1] = max( matrix[i1][i2 + 1], matrix[i1 + 1][i2])
    return matrix[len_s1][len_s2]

if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(str(result) + '\n')
