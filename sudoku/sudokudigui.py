# -*- coding: utf-8 -*-
#! python.exe

import os
import codecs
import re
import sys
import copy
import time
import logging

print("hello python")

ArrFilledZero = [0,0,0,0,0,0,0,0,0]

# Arr0 = [8,0,0, 0,0,0, 0,0,0]
# Arr1 = [0,0,3, 6,0,0, 0,0,0]
# Arr2 = [0,7,0, 0,9,0, 2,0,0]
# Arr3 = [0,5,0, 0,0,7, 0,0,0]
# Arr4 = [0,0,0, 0,4,5, 7,0,0]
# Arr5 = [0,0,0, 1,0,0, 0,3,0]
# Arr6 = [0,0,1, 0,0,0, 0,6,8]
# Arr7 = [0,0,8, 5,0,0, 0,1,0]
# Arr8 = [0,9,0, 0,0,0, 4,0,0]

# Arr0 = [0,4,0,0,0,3,5,0,0]
# Arr1 = [0,2,0,9,0,0,4,0,0]
# Arr2 = [0,0,6,0,0,0,0,0,0]
# Arr3 = [4,0,0,0,0,9,0,0,1]
# Arr4 = [0,3,0,7,0,0,0,2,0]
# Arr5 = [9,0,0,0,0,0,0,0,8]
# Arr6 = [0,0,0,0,0,0,3,0,0]
# Arr7 = [0,0,9,0,0,4,0,8,0]
# Arr8 = [0,0,8,1,0,0,0,7,0]

# arrBaseNum = [Arr0, Arr1, Arr2, Arr3, Arr4, Arr5, Arr6, Arr7, Arr8]
# arrBaseNum = [
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0]
# ]

arrBaseNum = [
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
]

# arrBaseNum = [
# [0,0,0,0,1,0,0,5,4],
# [8,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0],
# [6,5,0,4,0,0,0,0,0],
# [0,0,0,0,0,2,7,3,0],
# [0,0,0,0,0,0,0,0,0],
# [2,1,0,0,0,0,8,0,0],
# [7,0,0,0,0,0,3,0,0],
# [0,0,0,3,5,0,0,0,0]
# ]

len_ArrBase = len(arrBaseNum)
len_nine = 9

pu = arrBaseNum
def isvalid(i, j):
	n = pu[i][j];
	query = [ 0, 0, 0, 3, 3, 3, 6, 6, 6 ];

	for t in range(0,len_nine):
		if (t != i and pu[t][j] == n or t != j and pu[i][t] == n):
			return 0

	for t in range(query[i], query[i] + 3):
		for u in range(query[j], query[j] + 3):
			if ((t != i or u != j) and pu[t][u] == n):
				return 0

	return 1

def output():
	print("Solution is:");

	for i in range(0, len_nine):
		tempstr = ""
		for j in range(0, len_nine):
			tempstr += str(pu[i][j]) + " "
		print(tempstr)
	print("---get this result time---", float('%.2f' % (time.clock() - time_begin)))

def Try(n):
	if (n == 81):
		output()
		return
	i = n / 9
	j = n % 9

	if (pu[i][j] != 0):
		Try(n + 1)
		return

	for k in range(0,len_nine):
		pu[i][j] += 1;
		if (isvalid(i, j)):
			Try(n + 1)

	pu[i][j] = 0

time_begin = time.clock()
print("---start---", float('%.2f' % (time.clock() - time_begin)))
Try(0)
print("---get result---", float('%.2f' % (time.clock() - time_begin)))