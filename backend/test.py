import json
import csv
from csv import reader, writer
import math


# def bestFieldGoalPercentage():
#     allGGPercentages = []
#     playerNames = []
#     sorted = []
#     with open('dataset/games_details.csv') as csvfile: 
#         readCSV = csv.reader(csvfile, delimiter=',')
#         for row in readCSV:
#             if len(row[7]) == 0 and len(row[10]) > 0: #player suited up and they attempted at least 10 shots
#                 attempted_shots = row[10]
#                 attempted_shots = attempted_shots[:-2]
#                 attempted_shots = int(attempted_shots)
#                 if attempted_shots > 20:
#                     FG_PCT = row[11]
#                     FG_PCT = float(FG_PCT) #could get error here for field goal %   
#                     allGGPercentages.append(FG_PCT)
#                     playerNames.append(row[5])
#                     sorted.append(FG_PCT)
#             #row = row + 1

#     sorted.sort()
#     print(sorted)

    
#     for i in range(1,22): 
#         print(sorted[-i])
#         indexValue = allGGPercentages.index(sorted[-i])
#         hehe69 = playerNames[indexValue]
#         print(hehe69) 
#         i = i + 1 
#     return("hehe")


# # Top 10 3P Shooters in a Game
# def topTen3Pointers():
#     myDict = {}
#     finalDict = {}
#     with open('dataset/games_details.csv') as csvfile: 
#         readCSV = csv.reader(csvfile, delimiter=',')
#         for row in readCSV:
#             if len(row[7]) == 0 and len(row[14]) > 0: #makes sure player didn't sit out, or that player didn't have a 3point average of 0

#                 # FG3_PCT = FG3_PCT 
#                 attempted3Points = row[13]
#                 attempted3Points = attempted3Points[:-2]
#                 attempted3Points = int(attempted3Points)
#                 if attempted3Points > 10:
#                     FG3_PCT = row[14] #percentage of 3 pointers made
#                     myDict[row[5]] = row[14]    #appending to dictionary, row[5] = playerName, row[14] = 3Point%
#     sort_Dict = sorted(myDict.items(), key=lambda x: x[1])
#     for i in range(1,11):
#         finalDict[i] = sort_Dict[-i]
#     print(finalDict)
# topTen3Pointers()

                # attempted_shots = row[10]
                # attempted_shots = attempted_shots[:-2]
                # attempted_shots = int(attempted_shots)
                # percent = row[11]
                # percent = float(percent)

def topTenBlocks():
    myDict = {}
    finalDict = {}
    with open('dataset/games_details.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row[7]) == 0 and row[23] != "0.0" and row[23] != "" : #makes sure player didn't sit out, or that player didn't have 0 blocks in the game
                blocks = row[23]
                blocks = blocks[:-2]
                blocks = int(blocks)
                if blocks > 9:                  #filter out those who didn't block much to quicken runtime
                    myDict[row[5]] = row[23]    #appending to dictionary, row[5] = playerName, row[14] = 3Point%
    sort_Dict = sorted(myDict.items(), key=lambda x: x[1])
    for i in range(1,11):
        finalDict[i] = sort_Dict[-i]
    # print(finalDict)
    return(finalDict)

topTenBlocks()


# orders = {
# 	'cappuccino': 54,
# 	'latte': 56,
# 	'espresso': 72,
# 	'americano': 48,
# 	'cortado': 41
# }

# sort_orders = sorted(orders.items(), key=lambda x: x[1])

# for i in sort_orders:
# 	print(i[0], i[1])