from random import randint
from pylab import *
import random as rd
import math as m
import itertools

A = [2,3,7,8,9,10,12,14,15,16,17]
B = [2,3,4,5,8,9,10,11,13,14,16,17]
C = [1,3,4,5,6,7,9,10,11,13,14,17]
D = [1,5,6,7,10,11,13,17]
unit = [A, B, C, D]
unitNames = ['A', 'B', 'C', 'D']
unitCombinations = list(itertools.permutations(unit,len(unit)))
unitCombinationsNames = list(itertools.permutations(unitNames,len(unitNames)))

students = 17
trials = 10000
result = []
results = []
check = []

def rollTheDice(room, check):
	randNumber = randint(0, len(room))
	if check.count(room[randNumber]) == 0:
		check.append(room[randNumber])
		result.append(room[randNumber])
	else:
		rollTheDice(room, check)

def runSimulation(unit, trials):
	for _ in range(trials):
		for r in unit:
			rollTheDice(r, check)
		del check[:]

def runSimulations():
    for i in unitCombinations:
        runSimulation(i, trials)
        printList(result)
        del result[:]

def printList(result):
	for i in range(students):
		print i+1,
		print float(result.count(i+1))/float(trials)

def printCombos(result):
	for i in result:
		print i

runSimulations()
printCombos(unitCombinationsNames)
