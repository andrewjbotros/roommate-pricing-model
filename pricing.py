from random import randint

roomA = [12,3,5,7,9,10,12,14,15,16]
roomB = [12,3,4,6,7,8,10,11,12,13,14]
roomC = [1,4,5,6,7,9,10,11,13,14]
roomD = [12,5,7,8,10,11,13,14]
result = []
total = []

for _ in range(10):
	randNumber = roomA[randint(0, len(roomA) - 1)]
	print randNumber
	result.append(randNumber)
	print result


