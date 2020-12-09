import json
import csv
from csv import reader, writer
import math



def searchTeams():
    m = request.get_json()
    x = json.dumps(m)
    y = json.loads(x)
    myteam = str((y["team"]["teamName"]))
    myseason = str((y["team"]["season"]))
    with open('dataset/teams.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == myteam:
                    teamID = row[1]
    myList = list()
    with open('dataset/games.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[5] == season:
                if row[3] == '1610612747':
                    strz = str(row[7] + row[8] + row[9] + row[10] + row[11] + row[12])
                    myList.append(strz)
    print(myList)

searchTeams()