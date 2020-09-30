#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count_strings = len(s)

    for i in range(n):
        letter = s[i]

        if i > 0:
            j = i        
            while j < n - 1:
                j += 1
                if s[j] == letter:
                    count_strings += 1
                else:
                    break

        outset = 0
        second_letter = None
        # print('i', i) b aba aabaa
        while i + outset + 1 < n and i - outset - 1 >= 0:
            outset += 1
            if letter != s[i + outset] and s[i + outset] == s[i - outset]:
                if second_letter == None:
                    # print('if 1', s[i + outset], i+ outset, s[i - outset], i - outset)
                    count_strings += 1
                    print(s[i - outset:i + outset + 1], i, outset)
                    second_letter = s[i + outset]
                elif s[i + outset] == second_letter and s[i - outset] == second_letter:
                    # print('if 2')
                    count_strings += 1
                    print(s[i - outset:i + outset + 1], i, outset)
                else:
                    break
            else:
                break
    return count_strings


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(str(result) + '\n')
