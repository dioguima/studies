#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    
    char_occurrences = dict(collections.Counter(s))
    count_occurrences =  dict(collections.Counter(char_occurrences.values()))
    
    
    if len(count_occurrences.items()) == 1: 
        return 'YES'

    lowest_char_count = min(char_occurrences.values())

    print('lowest_char_count', lowest_char_count)
    dictionary = dict(count_occurrences.items())
    print(dictionary)
    flag_change_arr = False
    for k, occurrences in dictionary.items():
        if int(k) == 1 and occurrences == 1:
            flag_change_arr = True
            print('passou aqui')
            break
    
    if flag_change_arr:
        array_values = list(count_occurrences.values())
        array_values.remove(1)
        lowest_char_count = min(array_values)
        dictionary[1] = 0
    print('lowest_char_count', lowest_char_count)

    flag_removed_used = False
    for k, occurrences in count_occurrences.items():
        print('k', k)        
        print('occurrences', occurrences)        
        print('flag_removed_used', flag_removed_used)
        print()

        if int(k) > lowest_char_count and k != lowest_char_count and occurrences != 0:
            if occurrences > 1 or flag_removed_used or int(k) - lowest_char_count > 1:
                return 'NO'
            elif occurrences == 1 and int(k) - lowest_char_count == 1:
                flag_removed_used = True

    return 'YES'


if __name__ == '__main__':

    s = input()

    result = isValid(s)

    print(result + '\n')
