#!/bin/python3

import math
import os
import random
import re
import sys

def getMedianEven(d):
    half_point_lower = int(d / 2)
    half_point_higher = half_point_lower - 1
    return lambda values: (values[half_point_lower] + values[half_point_higher]) / 2 
    # half_point_lower = int(len(values) / 2)
    # half_point_higher = int(len(values) / 2) + 1
    # return (values[half_point_lower] + values[half_point_higher]) / 2

def getMedianOdd(d):
    half_point = int(d / 2)
    return lambda values: values[half_point]

def get_index_to_insert(arr, start, end, n_to_find):

    
    if end - start == 1:
        if n_to_find > arr[start]:
            return start + 1
        else:
            return start

    middle = int((end - start) / 2)
    # print(f'start: {start}\nend: {end}\narr: {arr[start:end]}\nmiddle: {str(middle)}\n')
    if n_to_find > arr[middle]:
        return get_index_to_insert(arr, middle + 1, end, n_to_find)
    else:
        return get_index_to_insert(arr, start, middle, n_to_find)

def insert_item_in_order(arr, number):
    # print(number)
    index = get_index_to_insert(arr, 0, len(arr), number) - 1
    
    return arr[:-index] + [number] + arr[-index:]
    # print(f'item to insert: {number}\nindex returned: {index}\nnew array: {arr}')
    # print('#####')

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    d_values = []
    for i in range(d):
        d_values.insert(0, expenditure[i])

    d_values.sort()
    count_notifications = 0

    if d % 2 == 0:
        getMedian = getMedianEven(d)
    else:
        getMedian = getMedianOdd(d)

    for i in range(d, len(expenditure)):
        median = getMedian(d_values)
        current_expenditure = expenditure[i]
        # print(i, current_expenditure, median, d_values)

        if current_expenditure >= 2 * median:
            # print(i, current_expenditure, median, d_values)
            count_notifications += 1
        
        d_values.remove(expenditure[i - d])
        d_values = insert_item_in_order(d_values, current_expenditure)
        # d_values.insert(0, current_expenditure)
        # d_values.sort()
    return count_notifications

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
