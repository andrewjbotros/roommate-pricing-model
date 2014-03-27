from random import randint
from pylab import *

roomA = [2,3,7,8,9,10,12,14,15,16,17]
roomB = [2,3,4,5,8,9,10,11,13,14,16,17]
roomC = [1,3,4,5,6,7,9,10,11,13,14,17]
roomD = [1,5,6,7,10,11,13,17]
unit = [roomA, roomB, roomC, roomD]
students = 17
trials = 1000
result = []
check = []
probabilities = []

def rollTheDice(room, check):
	randNumber = randint(0, len(room))
	if check.count(room[randNumber]) == 0:
		check.append(room[randNumber])
		result.append(room[randNumber])
	else:
		rollTheDice(room, check)

for _ in range(trials):
	for r in unit:
		rollTheDice(r, check)
	check = []

for i in range(students):
	probabilities.append(result.count(i+1))
	print i + 1,
	print float(result.count(i+1))/float(trials)

print probabilities