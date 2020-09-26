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
    group_by_occurrences =  dict(collections.Counter(char_occurrences.values()))

    if len(group_by_occurrences.items()) == 1: 
        return 'YES'

    min_occurrences_char = min(char_occurrences.values())

    group_by_occurrences_dict = dict(group_by_occurrences.items())
    flag_change_arr = False
    for number, occurrences in group_by_occurrences_dict.items():
        if int(number) == 1 and occurrences == 1:
            flag_change_arr = True
            break
    
    if flag_change_arr:
        array_values = list(group_by_occurrences_dict.values())
        array_values.remove(1)
        min_occurrences_char = min(array_values)
        group_by_occurrences_dict[1] = 0

    filtered_list = list(filter(lambda t: t[1] > 0, group_by_occurrences_dict.items()))
    if len(filtered_list) == 1: 
        return 'YES'

    flag_removed_used = False
    for number, occurrences in group_by_occurrences_dict.items():
        if int(number) > min_occurrences_char and occurrences != 0:
            if flag_removed_used or occurrences > 1 or int(number) - min_occurrences_char > 1:
                return 'NO'
            elif occurrences == 1 and int(number) - min_occurrences_char == 1:
                flag_removed_used = True

    return 'YES'


if __name__ == '__main__':

    s = input()

    result = isValid(s)

    print(result + '\n')
