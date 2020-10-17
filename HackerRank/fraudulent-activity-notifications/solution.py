#!/bin/python3

import math
import os
import random
import re
import sys

def getMedianEven(d):
    half_point_lower = int(d / 2)
    half_point_higher = half_point_lower + 1
    return lambda values: (values[half_point_lower] + values[half_point_higher]) / 2
    # half_point_lower = int(len(values) / 2)
    # half_point_higher = int(len(values) / 2) + 1
    # return (values[half_point_lower] + values[half_point_higher]) / 2

def getMedianOdd(d):
    half_point = int(d / 2)
    return lambda values: values[half_point]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    d_values = []
    for i in range(d):
        d_values.insert(0, expenditure[i])

    d_values.sort()
    count_notifications = 0

    if d % 2 == 0:
        # getMedian = lambda values: (values[int(len(values) / 2)] + values[int(len(values) / 2) + 1]) / 2
        getMedian = getMedianEven(d)
    else:
        # getMedian = lambda values: values[int(len(values) / 2)]
        getMedian = getMedianOdd(d)

    for i in range(d, len(expenditure)):
        median = getMedian(d_values)
        current_expenditure = expenditure[i]
        # print(i, current_expenditure, median, d_values)

        if current_expenditure >= 2 * median:
            # print(i, current_expenditure, median, d_values)
            count_notifications += 1

        d_values.remove(expenditure[i - d])
        # for j in range(d - 1):
        #     if d_values[j] >= current_expenditure:
        #         d_values.insert(j, current_expenditure)
        #         break
        #     elif j == d - 2:
        #         d_values.insert(j, current_expenditure)

        d_values.insert(0, current_expenditure)
        d_values.sort()

    return count_notifications

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
