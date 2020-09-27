#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    removed = 0
    for i in range(len(s)):
        if i < len(s) - 1 and s[i + 1] == s[i]:
            removed += 1
    return removed 


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result))

    
