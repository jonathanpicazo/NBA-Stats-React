import csv
from csv import reader, writer

myDict = {}
with open("hype.txt") as fd:
    for line in fd:
        a = line.split(',')
        name = a[0]
        stat = a[1].strip()
        myDict[name] = stat

print(myDict)

with open("bestgame.txt") as fd:
    for line in fd:
        a = line.split(',')
        name = a[0]
        stat = a[1].strip()
        myDict[name] = stat
print(myDict)

with open("block.txt") as fd:
    for line in fd:
        a = line.split(',')
        name = a[0]
        stat = a[1].strip()
        myDict[name] = stat
print(myDict)

with open("shooters.txt") as fd:
    for line in fd:
        a = line.split(',')
        name = a[0]
        stat = a[1].strip()
        myDict[name] = stat
print(myDict)

with open("besthome.txt") as fd:
    for line in fd:
        a = line.split(',')
        name = a[0]
        stat = a[1].strip()
        myDict[name] = stat
print(myDict)
        