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

def initArrByZero(i,j):
	temparr = []
	for x1 in range(0,i):
		tarr = []
		for y2 in range(0,j):
			tarr.append(0)
		temparr.append(tarr)
	return temparr

class Node(object):
	col = 0
	row = 0
	value = []
	"""docstring for SudoOne"""
	def __init__(self):
		super(Node, self).__init__()
		self.value = copy.deepcopy(ArrFilledZero)
		self.value.append(0)

LenNine = 9
def Inspection(sudo):
	temp = copy.deepcopy(ArrFilledZero)
	temp.append(0)
	for i in range(0, LenNine):
		for j in range(0, LenNine):
			if (sudo[i][j] != 0):
				for m in range(0, LenNine+1):
					temp[m] = 0
				for m in range(0, LenNine):
					if sudo[i][m] !=0:
						if temp[sudo[i][m]] == 0:
							temp[sudo[i][m]]=1
						else:
							return False
					# 检查所在列数字是否合法
					for m in range(0, LenNine+1):
						temp[m]=0
					for m in range(0, LenNine):
						if sudo[m][j] !=0:
							if temp[sudo[m][j]] ==0:
								temp[sudo[m][j]] = 1
							else:
								return False

						# 检查所在小九宫格中数字是否合法(i,j)与小九宫格到位置（i/3*3,j/3*3） 转换。
						for m in range(0, LenNine+1):
							temp[m]=0
						for m in range(0, LenNine):
							for n in range(0, 3):
								if sudo[int(i/3)*3+m][int(j/3)*3+n] != 0:
									if temp[sudo[int(i/3)*3+m][int(j/3)*3+n]]==0:
										temp[sudo[int(i/3)*3+m][int(j/3)*3+n]]=1
									else:
										return False
	return True

def Initialization_col_row(sudo, node_sudo):
	m = 0
	for i in range(0, LenNine):
		for j in range(0, LenNine):
			if sudo[i][j]==0:
				node_sudo[m].col = i
				node_sudo[m].row = j
				m += 1

def Blank_number(sudo):                                     #计算所给数独中待填入的空白数
    num = 0
    for i in range(0,9):
        for j in range(0,9):
            if(sudo[i][j]==0):
                num += 1
    return num

def Find_value(sudo, node_sudo):                               # 找到合法的解。   value[10],第一个值存总共可以由多少个元素。 可以取得值value=0，否则=1。
	i = node_sudo.col
	j = node_sudo.row

	for m in range(0, 10):
		node_sudo.value[m] = 0
	for m in range(1, 10):
		node_sudo.value[ sudo[i][m-1] ] = 1                  #筛选行方向的值
		node_sudo.value[ sudo[m-1][j] ] = 1                  #筛选列方向的值

	for m in range(0, 3):                               	#筛选小九宫格方向的值
		for n in range(0, 3):
			node_sudo.value[sudo[int(i/3)*3+m][int(j/3)*3+n]]=1

	node_sudo.value[0] = 0                                           #node->value[0]记录候选值个数，前面的循环可能会修改掉它，需要重新赋0值
	for m in range(1, 10):
		if node_sudo.value[m] == 0:
			node_sudo.value[0] += 1

	bFind = False
	for m in range(1, 10):                                            #找到第一个可以取的值////////////////////////////////////////
		if node_sudo.value[m] == 0:
			node_sudo.value[m] = 1
			node_sudo.value[0] -= 1
			bFind = True
			break

	#返回候选值m，若无候选值可用，返回错误标记-1
	if not bFind:
		return -1
	else:
		return m

def Print_sudo(sudo):
	for i in range(0,9):
		tempstr = ""
		for j in range(0,9):
			tempstr += str(sudo[i][j]) + "  "
		print(tempstr)
	print("---get this result time---", float('%.2f' % (time.clock() - time_begin)))

def Solving(sudo, num_of_empty, node_sudo):               #num_of_empty  为总共空格数。
	k = 0       #记录已经求得了几个解。
	number = 1  #从第一个空格数开始求解。

	while( 0 < number and number <= (num_of_empty+1)):
		# print("node_sudo:", number, len(node_sudo))
		i = -1;
		j = -1;
		if (number - 1) < len(node_sudo):
			i = node_sudo[number-1].col
			j = node_sudo[number-1].row
		# print("node_sudo:",i,j)
		if number == num_of_empty+1:
			tempaaa = 1
		if number == 3:
			tempaaa = 1

		if (number>num_of_empty):
			k += 1
			count = 0
			for i in range(0, num_of_empty):
				if node_sudo[i].value[0] == 0:
					count += 1
			#//////////第一种情况//////////////////////////////////// 最后一次试探 刚好是得到所有解。提前结束
			if (count==num_of_empty):
				print("this is", k, "answer:")
				Print_sudo(sudo)
				print("already get all results")
				number += 1
			elif count != num_of_empty:                    #向前回溯求解。。
				print("this is", k, "answer:")
				Print_sudo(sudo)
				number -= 1
		elif ( 0<number  and  number<=num_of_empty ):
			if (sudo[i][j] != 0):
				if node_sudo[number-1].value[0] == 0:
					sudo[i][j] = 0
					number -= 1
				elif node_sudo[number-1].value[0] != 0:
					for index in range(1, 10):
						if node_sudo[number-1].value[index] == 0:
							sudo[i][j] = index
							node_sudo[number-1].value[index] = 1
							node_sudo[number-1].value[0] -= 1
							break
					number += 1
			elif(sudo[i][j] == 0):
				sudo[i][j] = Find_value(sudo, node_sudo[number-1])
				if (sudo[i][j] == -1):
					sudo[i][j] = 0
					number -= 1
				elif (sudo[i][j] != -1):
					number += 1
	if (number <= 0):
		if(k == 0):
			print("no valid result")
		if(k != 0):
			print("already get all results")

def sudoku(sudo):
	sudo99 = initArrByZero(LenNine, LenNine)
	number_of_empty = 0
	if Inspection(sudo):
		print("Is Invalid!!!")
		exit(1)
	number_of_empty=Blank_number(sudo);				#计算需要填入数的个数
	node_sudu = []
	for x in range(0, number_of_empty):
		node_sudu.append( Node() )

	Initialization_col_row(sudo, node_sudu)			#确定Node结构体重每一个元素的  col 和row 的值。
	Solving(sudo, number_of_empty, node_sudu)

time_begin = time.clock()
print("---start---", float('%.2f' % (time.clock() - time_begin)))
sudoku(arrBaseNum)
print("---get result---", float('%.2f' % (time.clock() - time_begin)))