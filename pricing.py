from random import randint
from pylab import *

roomA = [2,3,7,8,9,10,12,14,15,16,17]
roomB = [2,3,4,5,8,9,10,11,13,14,16,17]
roomC = [1,3,4,5,6,7,9,10,11,13,14,17]
roomD = [1,5,6,7,10,11,13,17]
unit1 = [roomA, roomB, roomC, roomD]
unit2 = [roomA, roomB, roomD, roomC]
unit3 = [roomA, roomC, roomB, roomD]
unit4 = [roomA, roomC, roomD, roomB]
unit5 = [roomA, roomD, roomB, roomC]
unit6 = [roomA, roomD, roomC, roomB]
students = 17
trials = 10000
result = []
check = []

def rollTheDice(room, check):
	randNumber = randint(0, len(room))
	if check.count(room[randNumber]) == 0:
		check.append(room[randNumber])
		result.append(room[randNumber])
	else:
		rollTheDice(room, check)

def orderTheDraw(unit, trials):
	for _ in range(trials):
		for r in unit:
			rollTheDice(r, check)
		del check[:]

orderTheDraw(unit6, trials)

for i in range(students):
	print i + 1,
	print float(result.count(i+1))/float(trials)
