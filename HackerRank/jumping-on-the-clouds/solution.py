#!/bin/python3

import math
import os
import random
import re
import sys

# P 0 1 2 3 4 5 6
# V 0 0 1 0 0 1 0

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	jumps = 0
	currentPosition = 0
	while currentPosition < len(c) - 1:
		if currentPosition + 2 < len(c) and c[currentPosition + 2] == 0:
			jumps += 1
			currentPosition += 2
		elif currentPosition + 1 < len(c) and c[currentPosition + 1] == 0:
			jumps += 1
			currentPosition += 1
	return jumps


if __name__ == '__main__':
	
	n = int(input())

	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c)

	print(str(result) + '\n')
