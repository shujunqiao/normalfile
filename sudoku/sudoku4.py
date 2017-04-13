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

def mylog(arg1, *arg2):
	tempstr = arg1
	for x in arg2:
		tempstr += " " + str(x)
	print(tempstr)
	logging.info(tempstr)

def checkArrIsOk(arr):
    sum = 0
    for x in arr:
        sum = sum + x
    if sum == 45:
        return True
    return False

LenOfSudo = 3
ArrFilledNums = [1,2,3,4,5,6,7,8,9]
ArrFilledZero = [0,0,0,0,0,0,0,0,0]
def checkLineIsValid(arr):
	tempArr = copy.deepcopy(ArrFilledZero)
	for x in arr:
		tempArr[x] = tempArr[x] + 1
		if tempArr[x] > 1:
			return False
	return True

def getRemainderNums(arr):
	tempArr = copy.deepcopy(ArrFilledNums)
	for x in arr:
		if x != 0:
			tempArr.remove(x)
	return tempArr

def swap(arr, k, m):
	temp = arr[k]
	arr[k] = arr[m]
	arr[m] = temp

def perm(arr, k, m):
	tempArr = []
	if k == m:
		for i in range(0, m):
			tempArr.append(arr[i])
	else:
		for j in range(k, m):
			swap(arr, j, k)
			retArr = perm(arr, k+1, m)
			if type(retArr[0]) == type(0):
				tempArr.append(retArr)
			else:
				for x in retArr:
					tempArr.append(x)
			swap(arr, j, k)
	return tempArr

def insertArr(arr1, arr2):
	for x in range(0, len(arr2)):
		if arr2[x] != 0 and arr1.count(arr2[x]) == 0:
			arr1.insert(x, arr2[x])

def checkOneLine(line, arr):
	for item in arr:
		if line.count(item) > 0:
			return False
	return True

def removeSameNum(arr1, arr2):
	for item in arr2:
		if arr1.count(item):
			arr1.remove(item)

def checkArrIsEqual(arr1, arr2):
	for item in arr1:
		if arr2.count(item) == 0:
			return False
	return True

class SudoOne(object):
	arr = []
	remainedNums = []
	permRemainedArr = []
	permRemainedOriginArr = []
	allMaybeCombiArr = []
	checkArr = []
	maybeArr = []
	"""docstring for SudoOne"""
	def __init__(self, arg):
		super(SudoOne, self).__init__()
		self.arr = copy.deepcopy(arg)

	def log(self, str):
		mylog("log:", str, self.arr)

	def checkSelf(self):
		mylog("log:", self.arr)
		ret = checkArrIsOk(self.arr)
		return ret

	def getHArr(self, idx):
		return self.arr[idx*3 : (idx+1)*3]

	def getVArr(self, idx):
		return [self.arr[idx], self.arr[idx+3], self.arr[idx+6]]

	def getLineByIdx(self, idx):
		if idx < 3:
			return self.getHArr(idx)
		else:
			return self.getVArr(idx - 3)

	def fillAllNum(self):
		remainedNums = getRemainderNums(self.arr)
		permRemained = perm(remainedNums, 0, len(remainedNums))
		for arr in permRemained:
			insertArr(arr, self.arr)

		self.permRemainedOriginArr = permRemained

	def checkHV(self, sudu, arr2):
		checkResult = True
		for i in range(0, len(arr2)):
			if len(arr2) > 0:
				checkResult = checkResult & checkOneLine(sudu.getLineByIdx(i), arr2[i])
		return checkResult

	def checkArr(self, arr):
		if len(self.permRemainedOriginArr) == 0:
			self.fillAllNum()
		self.permRemainedArr = copy.deepcopy(self.permRemainedOriginArr)
		rmNum = 1
		while rmNum:
			rmNum = 0
			for item in self.permRemainedArr:
				checkResult = self.checkHV(SudoOne(item), arr)
				if not checkResult:
					self.permRemainedArr.remove(item)
					rmNum = rmNum + 1

	def getMaybenums(self, pos):
		if len(self.remainedNums) == 0:
			self.remainedNums = getRemainderNums(self.arr)
		tempMaybe = copy.deepcopy(self.remainedNums)
		# check H
		hidx = int(pos/LenOfSudo)
		removeSameNum(tempMaybe, self.checkArr[hidx])
		# check V
		vidx = int(pos%LenOfSudo)
		removeSameNum(tempMaybe, self.checkArr[vidx + 3])
		return tempMaybe

	def checkArrNoUse(self, arr):
		self.checkArr = copy.deepcopy(arr)
		self.maybeArr = []
		for i in range(0, len(self.arr)):
			if self.arr[i] != 0:
				self.maybeArr.append([])
			else:
				self.maybeArr.append(self.getMaybenums(i))

	def checkMaybeIsValid(self):
		for item in self.maybeArr:
			if len(item) > 0 and self.maybeArr.count(item) > len(item):
				# mylog("self.maybeArr:", self.maybeArr)
				return False
		return True

	def getAllMaybeCombi(self):
		# mylog("self.maybeArr:", self.maybeArr)
		self.allMaybeCombiArr = []
		temp_len = 1
		for i in range(0, len(self.maybeArr)):
			if len(self.maybeArr[i]) != 0:
				temp_len = temp_len * len(self.maybeArr[i])
				for k in range(len(self.allMaybeCombiArr), temp_len):
					self.allMaybeCombiArr.append([])
		# mylog("temp_len:", temp_len)

		len_used = 1
		for i in range(0, len(self.maybeArr)):
			temp_len = len(self.maybeArr[i])
			for j in range(0, len(self.allMaybeCombiArr)):
				if temp_len != 0:
					self.allMaybeCombiArr[j].append( self.maybeArr[i][(j / len_used) % temp_len] )
				else:
					self.allMaybeCombiArr[j].append( self.arr[i] )
			if temp_len != 0:
				len_used *= temp_len

		# checkArrIsOk
		rmNum = 1
		while rmNum:
			rmNum = 0
			for item in self.allMaybeCombiArr:
				checkResult = checkArrIsOk(item)
				if not checkResult:
					self.allMaybeCombiArr.remove(item)
					rmNum = rmNum + 1

		if len(self.allMaybeCombiArr) > 0:
			# checkArrIsValid
			# mylog("self.allMaybeCombiArr:", len(self.allMaybeCombiArr), "\n")
			rmNum = 1
			while rmNum:
				rmNum = 0
				for item in self.allMaybeCombiArr:
					for num in item:
						if item.count(num) > 1:
							if self.allMaybeCombiArr.count(item) > 0:
								self.allMaybeCombiArr.remove(item)
								rmNum = rmNum + 1

		if len(self.allMaybeCombiArr) > 0:
			# checkArrIsValid
			# mylog("self.allMaybeCombiArr:", len(self.allMaybeCombiArr), "\n")
			rmNum = 1
			while rmNum:
				rmNum = 0
				for item in self.allMaybeCombiArr:
					checkResult = self.checkHV(SudoOne(item), self.checkArr)
					if not checkResult:
						self.allMaybeCombiArr.remove(item)
						rmNum = rmNum + 1
		# if len(self.allMaybeCombiArr) > 0:
		# 	mylog("self.allMaybeCombiArr:", len(self.allMaybeCombiArr), "\n")

log_filename = "myapp123.log"
# clear file content
f = file(log_filename, "w")
f.write("")
f.close()

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=log_filename,
                filemode='w')


# Arr0 = [8,0,0,0,0,3,0,7,0]
# Arr1 = [0,0,0,6,0,0,0,9,0]
# Arr2 = [0,0,0,0,0,0,2,0,0]
# Arr3 = [0,5,0,0,0,0,0,0,0]
# Arr4 = [0,0,7,0,4,5,1,0,0]
# Arr5 = [0,0,0,7,0,0,0,3,0]
# Arr6 = [0,0,1,0,0,8,0,9,0]
# Arr7 = [0,0,0,5,0,0,0,0,0]
# Arr8 = [0,6,8,0,1,0,4,0,0]
# checkArr0 = [[],[6],[9,2],[],[5,9],[1,8]]
# checkArr1 = [[8],[3],[2,7],[1,5],[4],[5,7]]
# checkArr2 = [[8],[6],[7,9],[4,7],[1,3,6],[8]]
# checkArr3 = [[7],[4,5,7],[1,3],[8],[7,9],[3,1,8]]
# checkArr4 = [[5],[7],[3],[5,6],[9],[]]
# checkArr5 = [[5,7],[4,5],[1],[2,4],[6,1],[8]]
# checkArr6 = [[6,8],[1,5],[4],[8],[7,5],[3]]
# checkArr7 = [[1,6,8],[8,1],[9,4],[6,1],[9,4],[7,5]]
# checkArr8 = [[1],[8,5],[9],[2,7],[3],[]]

# Arr0 = [0,6,0,0,0,1,0,0,0]
# Arr1 = [9,0,1,0,0,0,0,0,0]
# Arr2 = [0,7,0,4,9,0,1,6,8]
# Arr3 = [0,3,0,0,2,0,0,0,5]
# Arr4 = [0,8,0,0,0,5,0,0,7]
# Arr5 = [6,5,9,0,1,0,8,2,4]
# Arr6 = [0,0,6,0,0,3,4,8,0]
# Arr7 = [0,5,4,8,0,6,0,1,9]
# Arr8 = [0,8,2,7,4,0,5,0,0]
# checkArr0 = [[1,7,9],[4,9],[1,6,8],[4],[2,3,8],[3,5,6]]
# checkArr1 = [[6,7],[1,4,9],[1,6,8],[8],[1,5,8],[4,5,6,7,9]]
# checkArr2 = [[1,6,9],[1],[],[5,6,7,8],[1,2,4,5,8],[2,4,9]]
# checkArr3 = [[5,6,8,9],[1,5],[2,4,7,8],[4],[6,8],[1,3,6]]
# checkArr4 = [[3,5,6,9],[1,2],[2,4,5,8],[8,9],[1,5],[1,4,6,9]]
# checkArr5 = [[3,8],[2,5],[5,7],[1,4,5,7],[4,6,7,8,9],[2,8]]
# checkArr6 = [[2,4,5,8],[4,6,7,8],[1,5,9],[],[2,3,6],[1,5]]
# checkArr7 = [[2,6,8],[3,4,7],[4,5,8],[9],[8],[1,7,5]]
# checkArr8 = [[4,5,6],[3,6,8],[1,4,8,9],[1,4,6,8],[1,2,5,6,7,9],[4,8,9]]

# Arr0 = [4,7,0,0,0,0,0,0,0]
# Arr1 = [0,0,0,1,0,0,0,4,0]
# Arr2 = [1,0,6,0,0,0,0,0,7]
# Arr3 = [0,0,0,6,0,0,0,0,8]
# Arr4 = [0,0,7,0,0,8,2,0,0]
# Arr5 = [0,1,0,0,7,0,0,0,0]
# Arr6 = [9,3,0,0,0,0,0,0,0]
# Arr7 = [0,0,0,7,8,0,0,0,9]
# Arr8 = [0,0,0,0,0,0,0,2,1]
# checkArr0 = [[1,6],[1],[4,7],[6,9],[3],[8]]
# checkArr1 = [[1,4,6,7],[],[7],[2,7],[8],[8,7,9]]
# checkArr2 = [[4,7],[1],[4],[],[1,2,7],[1]]
# checkArr3 = [[1,7],[7,8],[2],[4,9],[3,7],[]]
# checkArr4 = [[1],[6,7],[8],[1,7],[4,8],[9]]
# checkArr5 = [[7],[6,8],[2,8],[1],[2],[1,6,7]]
# checkArr6 = [[],[7,8],[1,2,9],[4,6],[7],[8]]
# checkArr7 = [[3,9],[],[1,2],[1,2],[4],[7,8]]
# checkArr8 = [[3,9],[7,8],[9],[1],[1,7],[6,7]]

Arr0 = [0,4,0,0,2,0,0,0,6]
Arr1 = [0,0,3,9,0,0,0,0,0]
Arr2 = [5,0,0,4,0,0,0,0,0]
Arr3 = [4,0,0,0,3,0,9,0,0]
Arr4 = [0,0,9,7,0,0,0,0,0]
Arr5 = [0,0,1,0,2,0,0,0,8]
Arr6 = [0,0,0,0,0,9,0,0,8]
Arr7 = [0,0,0,0,0,4,1,0,0]
Arr8 = [3,0,0,0,8,0,0,7,0]
checkArr0 = [[3,5],[4,9],[],[4,9],[3],[8,9]]
checkArr1 = [[4,5],[2,4],[6],[1,7],[],[4,9]]
checkArr2 = [[4,3],[2,9],[6],[3],[8,2,7],[1,8]]
checkArr3 = [[1,9],[7,2],[8],[],[2,4],[6,8,9]]
checkArr4 = [[1,4],[2,3],[8,9],[1,9],[],[3,4]]
checkArr5 = [[4,9],[3,7],[9],[3,4,5],[7,8],[]]
checkArr6 = [[3],[4,8],[1,7],[4,9],[2,3,4],[6]]
checkArr7 = [[3],[8,9],[7,8],[7,9],[],[3,9]]
checkArr8 = [[4,5],[2],[1,8],[],[4,9],[1,8]]


sudo8 = SudoOne(Arr8)
sudo6 = SudoOne(Arr6)
sudo0 = SudoOne(Arr0)
sudo1 = SudoOne(Arr1)
sudo4 = SudoOne(Arr4)
sudo7 = SudoOne(Arr7)
sudo5 = SudoOne(Arr5)
sudo3 = SudoOne(Arr3)
sudo2 = SudoOne(Arr2)


arr0_0 = []
arr1_0 = []
arr2_0 = []
arr3_0 = []
arr4_0 = []
arr5_0 = []
arr6_0 = []
arr7_0 = []
arr8_0 = []

# sudo8.checkArr(checkArr8)
# mylog("sudo8 permRemainedArr", len(sudo8.permRemainedArr))

time_begin = time.clock()
# --*** 找第八组 ***--
t_checkArr8 = copy.deepcopy(checkArr8)
print("\n t_checkArr8:", t_checkArr8, time.clock() - time_begin)

sudo8.checkArrNoUse(t_checkArr8)
if sudo8.checkMaybeIsValid():
	sudo8.getAllMaybeCombi()
print("sudo8 allMaybeCombiArr:", sudo8.allMaybeCombiArr, time.clock() - time_begin)

time_begin = time.clock()
for x8 in range(0, len(sudo8.allMaybeCombiArr)):
	# --*** 找到第九组 ***--
	arr8_0 = SudoOne(sudo8.allMaybeCombiArr[x8])
	mylog("sudo8 allMaybeCombiArr", x8, arr8_0.arr, int(time.clock() - time_begin))

	# --*** 找第七组... ***--
	t_checkArr6 = copy.deepcopy(checkArr6)
	for x in range(0,3):
		insertArr(t_checkArr6[x], arr8_0.getLineByIdx(x))

	mylog("--------------\n")

	sudo6.checkArrNoUse(t_checkArr6)
	if sudo6.checkMaybeIsValid():
		sudo6.getAllMaybeCombi()
	mylog("sudo6 allMaybeCombiArr", x8, (sudo6.allMaybeCombiArr), int(time.clock() - time_begin))

	bFind6 = False
	for x6 in range(0, len(sudo6.allMaybeCombiArr)):
		# --*** 找到第七组 ***--
		arr6_0 = SudoOne(sudo6.allMaybeCombiArr[x6])
		# mylog("sudo6 permRemainedArr", len(sudo6.permRemainedArr), x6, int(time.clock() - time_begin))

		# --*** 找第一组... ***--
		t_checkArr0 = copy.deepcopy(checkArr0)
		for x in range(3,6):
			insertArr(t_checkArr0[x], arr6_0.getLineByIdx(x))
		# mylog("\nt_checkArr0:", t_checkArr0)

		# mylog("\n--------------\n")
		# sudo0.checkArr(t_checkArr0)
		# mylog("sudo0 permRemainedArr ", x8, x6, len(sudo0.permRemainedArr), int(time.clock() - time_begin))
		sudo0.checkArrNoUse(t_checkArr0)
		if sudo0.checkMaybeIsValid():
			sudo0.getAllMaybeCombi()
		mylog("sudo0 allMaybeCombiArr", x8, x6, (sudo0.allMaybeCombiArr), int(time.clock() - time_begin))

		bFind0 = False
		for x0 in range(0, len(sudo0.allMaybeCombiArr)):
			# --*** 找到第一组 ***--
			arr0_0 = SudoOne(sudo0.allMaybeCombiArr[x0])
			# mylog("sudo0 permRemainedArr", len(sudo0.permRemainedArr), x0, int(time.clock() - time_begin))
			t_checkArr1 = copy.deepcopy(checkArr1)
			for x in range(0,3):
				insertArr(t_checkArr1[x], arr0_0.getLineByIdx(x))
			# mylog("\n t_checkArr1:", t_checkArr1)

			# mylog("\n--------------\n")
			# sudo1.checkArr(t_checkArr1)
			# print("sudo1.permRemainedArr:", len(sudo1.permRemainedArr))
			sudo1.checkArrNoUse(t_checkArr1)
			if sudo1.checkMaybeIsValid():
				sudo1.getAllMaybeCombi()
			mylog("sudo1 allMaybeCombiArr", x8, x6, x0, (sudo1.allMaybeCombiArr), int(time.clock() - time_begin))
			# ================-------------

			bFind1 = False
			for x1 in range(0, len(sudo1.allMaybeCombiArr)):
				# --*** 找到第二组 ***--
				arr1_0 = SudoOne(sudo1.allMaybeCombiArr[x1])
				# mylog("sudo1 permRemainedArr", len(sudo1.permRemainedArr), x1, int(time.clock() - time_begin))
				t_checkArr4 = copy.deepcopy(checkArr4)

				# mylog("arr1_0", arr1_0.arr, "---", t_checkArr4)
				for x in range(3,6):
					insertArr(t_checkArr4[x], arr1_0.getLineByIdx(x))
				# mylog("\n t_checkArr4:", t_checkArr4)

				# mylog("\n--------------\n")
				# sudo4.checkArr(t_checkArr4)
				sudo4.checkArrNoUse(t_checkArr4)
				if sudo4.checkMaybeIsValid():
					sudo4.getAllMaybeCombi()
				mylog("sudo4 allMaybeCombiArr", x1, (sudo4.allMaybeCombiArr), int(time.clock() - time_begin))
				# ================-------------

				bFind4 = False
				for x4 in range(0, len(sudo4.allMaybeCombiArr)):
					# --*** 找到第五组 ***--
					arr4_0 = SudoOne(sudo4.allMaybeCombiArr[x4])
					# mylog("sudo4 permRemainedArr", len(sudo4.permRemainedArr), x4, "time:", int(time.clock() - time_begin))

					# --*** 找第六组 ***--
					t_checkArr5 = copy.deepcopy(checkArr5)
					# mylog("t_checkArr5:", arr1_0.arr, arr4_0.arr, "---", t_checkArr5)
					for x in range(3,6):
						insertArr(t_checkArr5[x], arr8_0.getLineByIdx(x))
					for x in range(0,3):
						insertArr(t_checkArr5[x], arr4_0.getLineByIdx(x))
					# mylog("\n t_checkArr5:", t_checkArr5)
					# 
					sudo5.checkArrNoUse(t_checkArr5)
					if sudo5.checkMaybeIsValid():
						sudo5.getAllMaybeCombi()
					mylog("sudo5 allMaybeCombiArr", x4, (sudo5.allMaybeCombiArr), int(time.clock() - time_begin))

					# --*** 找第三组 ***--
					bFind5 = False
					for x5 in range(0, len(sudo5.allMaybeCombiArr)):
						arr5_0 = SudoOne(sudo5.allMaybeCombiArr[x5])

						bFind2 = False
						bFind3 = False
						t_checkArr2 = copy.deepcopy(checkArr2)
						# mylog("t_checkArr2:", arr0_0.arr, arr1_0.arr, arr8_0.arr, "---", t_checkArr2)
						for x in range(3,6):
							insertArr(t_checkArr2[x], arr5_0.getLineByIdx(x))
							insertArr(t_checkArr2[x], arr8_0.getLineByIdx(x))
						for x in range(0,3):
							insertArr(t_checkArr2[x], arr0_0.getLineByIdx(x))
							insertArr(t_checkArr2[x], arr1_0.getLineByIdx(x))
						# mylog("\n t_checkArr2:", t_checkArr2)
						# 
						sudo2.checkArrNoUse(t_checkArr2)
						if sudo2.checkMaybeIsValid():
							sudo2.getAllMaybeCombi()
						mylog("sudo2 allMaybeCombiArr", x5, (sudo2.allMaybeCombiArr), int(time.clock() - time_begin))
						if len(sudo2.allMaybeCombiArr) > 0:
							bFind2 = True
							arr2_0 = SudoOne(sudo2.allMaybeCombiArr[0])

						# --*** 找第四组 ***--
						t_checkArr3 = copy.deepcopy(checkArr3)
						# mylog("t_checkArr3:", arr0_0.arr, arr6_0.arr, arr4_0.arr, "---", t_checkArr3)
						for x in range(3,6):
							insertArr(t_checkArr3[x], arr0_0.getLineByIdx(x))
							insertArr(t_checkArr3[x], arr6_0.getLineByIdx(x))
						for x in range(0,3):
							insertArr(t_checkArr3[x], arr4_0.getLineByIdx(x))
							insertArr(t_checkArr3[x], arr5_0.getLineByIdx(x))
						# mylog("\n t_checkArr3:", t_checkArr3)
						# 
						sudo3.checkArrNoUse(t_checkArr3)
						if sudo3.checkMaybeIsValid():
							sudo3.getAllMaybeCombi()
						mylog("sudo3 allMaybeCombiArr", x5, (sudo3.allMaybeCombiArr), int(time.clock() - time_begin))
						if len(sudo3.allMaybeCombiArr) > 0:
							bFind3 = True
							arr3_0 = SudoOne(sudo3.allMaybeCombiArr[0])

						if bFind2 and bFind3:
							# --*** 找第八组 ***--
							t_checkArr7 = copy.deepcopy(checkArr7)
							# mylog("t_checkArr7:", arr1_0.arr, arr4_0.arr, arr6_0.arr, arr4_8.arr, "---", t_checkArr7)
							for x in range(3,6):
								insertArr(t_checkArr7[x], arr1_0.getLineByIdx(x))
								insertArr(t_checkArr7[x], arr4_0.getLineByIdx(x))
							for x in range(0,3):
								insertArr(t_checkArr7[x], arr6_0.getLineByIdx(x))
								insertArr(t_checkArr7[x], arr8_0.getLineByIdx(x))
							# mylog("\n t_checkArr7:", t_checkArr7)
							# 
							sudo7.checkArrNoUse(t_checkArr7)
							if sudo7.checkMaybeIsValid():
								sudo7.getAllMaybeCombi()
							mylog("sudo7 allMaybeCombiArr", x4, (sudo7.allMaybeCombiArr), int(time.clock() - time_begin))

							if len(sudo7.allMaybeCombiArr) > 0:
								arr7_0 = SudoOne(sudo7.allMaybeCombiArr[0])
								bFind7 = True
								bFind5 = True
								mylog("arr7_0:", arr0_0.arr, arr1_0.arr, arr2_0.arr, arr3_0.arr, arr4_0.arr, arr5_0.arr, arr6_0.arr, arr7_0.arr, arr8_0.arr)
								break
							else:
								bFind2 = False
								bFind3 = False
							continue

					if bFind5 and bFind7:
						bFind4 = True
						mylog("arr5_0:", arr0_0.arr, arr1_0.arr, arr2_0.arr, arr3_0.arr, arr4_0.arr, arr5_0.arr, arr6_0.arr, arr7_0.arr, arr8_0.arr)
						break
					else:
						bFind4 = False
				if bFind4:
					bFind1 = True
					break
				else:
					bFind1 = False
			if bFind1:
				bFind0 = True
				break
			else:
				bFind0 = False
		if bFind0:
			bFind6 = True
			break
		else:
			bFind6 = False
	if bFind6:
		break



mylog("------------------------\n")
mylog("arr0:", arr0_0.arr)
mylog("arr1:", arr1_0.arr)
if type(arr2_0) != type([]):
	mylog("arr2:", arr2_0.arr)
else:
	mylog("arr2:", arr2_0)
if type(arr3_0) != type([]):
	mylog("arr3:", arr3_0.arr)
else:
	mylog("arr3:", arr3_0)
mylog("arr4:", arr4_0.arr)
mylog("arr5:", arr5_0.arr)
mylog("arr6:", arr6_0.arr)
mylog("arr7:", arr7_0.arr)
mylog("arr8:", arr8_0.arr)
mylog("------------------------\n")
