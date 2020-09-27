#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    a_frequencies = [0 for i in range(26)]
    for i_a in range(len(a)):
        current_char_key = ord(a[i_a]) - ord('a')
        a_frequencies[current_char_key] += 1

    b_frequencies = [0 for i in range(26)]
    for i_b in range(len(b)):
        current_char_key = ord(b[i_b]) - ord('a')
        b_frequencies[current_char_key] += 1

    min_deletions = 0
    for i in range(26):
        difference = abs(a_frequencies[i] - b_frequencies[i])
        min_deletions += difference

    return min_deletions

if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(str(res) + '\n')
