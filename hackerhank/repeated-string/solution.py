#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedStringBruteForce(s, n):
    generated_string = s
    while len(generated_string) < n:
        generated_string += s
    generated_string = generated_string[:n]
    count_of_a = 0
    for i in range(len(generated_string)):
        current_char = generated_string[i]
        if current_char == 'a':
            count_of_a += 1
    return count_of_a

def repeatedString(s, n):
    exceeded_len = n % len(s)
    strings_in_total = int(n / len(s))
    count_of_a = strings_in_total * s.count('a') + s[:exceeded_len].count('a')
    return count_of_a

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')
