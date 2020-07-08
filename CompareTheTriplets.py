import math
import os
import random
import re
import sys

def compareTriplets(a,b):
	total_a = 0
	total_b = 0
	result = []

	for i,j in zip(a,b):
		if i > j:
			total_a += 1
		if j > i:
			total_b += 1
	result.append(total_a)
	result.append(total_b)

	return result

//fptr = open('path', 'w')
//a = list(map(int, input().rstrip().split()))
//b = list(map(int, input().rstrip().split()))
//result = compareTriplets(a,b)
//fptr.write(''.join(map(str, result)))
//fptr.write('\n')
//fptr.close()