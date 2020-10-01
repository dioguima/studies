#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    chars_count_s1 = {}
    chars_count_s2 = {}

    for i in range(len(s1)):
        char_s1 = s1[i]
        if chars_count_s1.get(char_s1) == None:
            chars_count_s1[char_s1] = 1
        else:
            chars_count_s1[char_s1] += 1
        
        char_s2 = s2[i]
        if chars_count_s2.get(char_s2) == None:
            chars_count_s2[char_s2] = 1
        else:
            chars_count_s2[char_s2] += 1

    # print(chars_count_s1)
    # print(chars_count_s2)

    for i in range(len(s1)):
        current_char_s1 = s1[i]
        current_best_s1 = current_char_s1
        # for j in range(len(s2)):
        #     if chars_count_s2.get(current_char_s1) != None:
                


    return -1

if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(str(result) + '\n')
