#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

def getMedianEven(d):
    half_point_lower = int(d / 2)
    half_point_higher = half_point_lower - 1
    return lambda values: (values[half_point_lower] + values[half_point_higher]) / 2 

def getMedianOdd(d):
    half_point = int(d / 2)
    return lambda values: values[half_point]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    d_values = sorted(expenditure[:d])
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
        
        del d_values[bisect.bisect_left(d_values, expenditure[i-d])]
        bisect.insort(d_values, current_expenditure)
    return count_notifications

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
