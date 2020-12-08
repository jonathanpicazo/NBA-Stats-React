from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import csv
from csv import reader, writer
import math

app = Flask(__name__)
CORS(app)

# Incremental Anal
@app.route('/UpdateBlocks', methods = ['GET', 'POST'])
def UpdateBlocks():
    if request.method == 'POST':
        playerblocks = {
        "JaVale McGee: ": "12.0",
        "Hassan Whiteside: ": "12.0",
        "Roy Hibbert: ": "11.0",
        "Joakim Noah: ": "11.0",
        "Larry Sanders: ": "10.0",
        "Anthony Davis: ": "10.0",
        "Serge Ibaka: ": "10.0",
        "Andrew Bynum: ": "10.0",
        "Dikembe Mutombo: ": "10.0",
        "Calvin Booth: ": "10.0"
        }
        print('here')
        #receive form from front end(playername,metric)
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        playername = str((y["player"]["playerName"])) + ': '
        metric = str((y["player"]["blk"]))
        print(playername)
        print(metric)
        playerblocks.update({playername: metric})
        sort_Dict = sorted(playerblocks.items(), key=lambda x: x[1])
        playerblocks.clear()
        for i in range(1,11):
            playerblocks[i] = sort_Dict[-i]
        print(playerblocks)
        return jsonify(playerblocks)

    elif request.method == 'GET':
        playerblocks = {
        "JaVale McGee: ": "12.0",
        "Hassan Whiteside: ": "12.0",
        "Roy Hibbert: ": "11.0",
        "Joakim Noah: ": "11.0",
        "Larry Sanders: ": "10.0",
        "Anthony Davis: ": "10.0",
        "Serge Ibaka: ": "10.0",
        "Andrew Bynum: ": "10.0",
        "Dikembe Mutombo: ": "10.0",
        "Calvin Booth: ": "10.0"
        }
        print('here')
        #receive form from front end(playername,metric)
        # m = request.get_json()
        # x = json.dumps(m)
        # y = json.loads(x)
        # playername = str((y["player"]["playerName"]))
        # metric = str((y["player"]["blk"]))
        # metric = float(metric)
        # print(playername)
        # print(metric)
        # playerblocks.update({playername: metric})
        sort_Dict = sorted(playerblocks.items(), key=lambda x: x[1])
        playerblocks.clear()
        for i in range(1,11):
            playerblocks[i] = sort_Dict[-i]
        print(playerblocks)
        return jsonify(playerblocks)

@app.route('/Updatethreeptgoal', methods = ['GET', 'POST'])
def Updatethreeptgoal():
    threeptgoal = {
    "Ty Lawson: ": "0.909",
    "Jodie Meeks: ": "0.818",
    "Yogi Ferrell: ": "0.818",
    "Jamal Murray: ": "0.818",
    "Rodrigue Beaubois: ": "0.818",
    "Mario Chalmers: ": "0.769",
    "Zach LaVine: ": "0.765",
    "Omri Casspi: ": "0.750",
    "Carmelo Anthony: ": "0.750",
    "Dorell Wright: ": "0.750"
    }
    #receive form from front end(playername,metric)
    if request.method == 'POST':
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        playername = str((y["player"]["playerName"])) + ': '
        metric = str((y["player"]["fg3_pct"]))
        threeptgoal.update({playername: metric})
    sort_Dict = sorted(threeptgoal.items(), key=lambda x: x[1])
    threeptgoal.clear()
    for i in range(1,11):
    	threeptgoal[i] = sort_Dict[-i]
    #print(playerblocks)
    return jsonify(threeptgoal)

@app.route('/Updatefg', methods = ['GET', 'POST'])
def Updatefg():
    fieldgoal = {
    "Amar'e Stoudemire: ": "0.741",
    "Paul George: ": "0.731",
    "Steve Nash: ": "0.714",
    "Andre Miller: ": "0.710",
    "Anthony Davis: ": "0.706",
    "Al Jefferson: ": "0.704",
    "Vince Carter: ": "0.704",
    "DeMarcus Cousins: ": "0.700",
    "Mo Williams: ": "0.692",
    "Carmelo Anthony: ": "0.692"
    }
    #receive form from front end(playername,metric)
    if request.method == 'POST':
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        playername = str((y["player"]["playerName"])) + ': '
        metric = str((y["player"]["fg_pct"]))
        fieldgoal.update({playername: metric})
    
    sort_Dict = sorted(fieldgoal.items(), key=lambda x: x[1])
    fieldgoal.clear()
    for i in range(1,11):
    	fieldgoal[i] = sort_Dict[-i]
    # print(fieldgoal)
    return jsonify(fieldgoal)

@app.route('/UpdatePlayerPerformance', methods = ['GET', 'POST'])
def UpdatePlayerPerformance():
    playerperformance = {
    "Klay Thompson: ": "560.07",
    "Shaquille O'Neal: ": "498.62",
    "Chandler Parsons: ": "441.49",
    "Jonas Valanciunas: ": "425.36",
    "Ty Lawson: ": "416.41",
    "Seth Curry: ": "415.57",
    "Tobias Harris: ": "395.53",
    "Chris Paul: ": "392.97",
    "Hassan Whiteside: ": "392.35",
    "Marc Gasol: ": "390.78"
    }
    #receive form from front end(playername,metric)
    if request.method == 'POST':
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        playername = str((y["player"]["playerName"])) + ': '
        metric = str((y["player"]["pp"]))
        playerperformance.update({playername: metric})
    sort_Dict = sorted(playerperformance.items(), key=lambda x: x[1])
    playerperformance.clear()
    for i in range(1,11):
    	playerperformance[i] = sort_Dict[-i]
    return jsonify(playerperformance)

@app.route('/UpdateTeamPerformance', methods = ['GET', 'POST'])
#TEAMS
def UpdateTeamPerformance():
    teamperformance = {
    "Nuggets: ": "168.0",
    "Hawks: ": "161.0",
    "Rockets: ": "158.0",
    "Washington: ": "158.0",
    "Nets: ": "157.0",
    "Spurs: ": "154.0",
    "Suns: ": "152.0",
    "Bucks: ": "151.0",
    "Thunder: ": "151.0",
    "Knicks: ": "151.0",
    }
    #receive form from front end(playername,metric)
    # try:
    #     print("Insert team name: ")
    #     playername = input()
    #     print("Insert metric amount: ")
    #     metric = input()
    # except EOFError as e:
    #     print(end="")
    # teamperformance.update({playername: metric})
    if request.method == 'POST':
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        playername = str((y["team"]["teamName"])) + ': '
        metric = str((y["team"]["homeDubs"]))
        teamperformance.update({playername: metric})
    sort_Dict = sorted(teamperformance.items(), key=lambda x: x[1])
    teamperformance.clear()
    for i in range(1,11):
    	teamperformance[i] = sort_Dict[-i]
    return jsonify(teamperformance)

@app.route('/UpdateTeamHype', methods = ['GET', 'POST'])
def UpdateTeamHype():
    teamhype =	{
    "Raptors: ": "15622.2",
    "Bucks: ": "15225",
    "Lakers: ": "14923.98",
    "76ers: ": "13454.05",
    "Clippers: ": "13380.12",
    "Heat: ": "13347.60",
    "Nuggets: ": "13292.90",
    "Celtics: ": "12943.68",
    "Mavericks: ": "11846.4",
    "Pacers: ": "11667.42"
    }
    #receive form from front end(playername,metric)
    # try:
    #     print("Insert team name: ")
    #     playername = input()
    #     print("Insert metric amount: ")
    #     metric = input()
    # except EOFError as e:
    #     print(end="")
    if request.method == 'POST':
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        playername = str((y["team"]["teamName"])) + ': '
        metric = str((y["team"]["ninjaHype"]))
        teamhype.update({playername: metric})
    
    sort_Dict = sorted(teamhype.items(), key=lambda x: x[1])
    teamhype.clear()
    for i in range(1,11):
    	teamhype[i] = sort_Dict[-i]
    return jsonify(teamhype)
    #print(teamhype)


@app.route('/bestHomeTeam', methods = ['GET', 'POST'])
#top ten scores in
def bestHomeTeam():
    myDict = {}
    finalDict = {}

    with open('dataset/games.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            if len(row[7]) > 0:
                teamPts = row[7]
                teamPts = int(float(teamPts))
                thresh = 116
                if teamPts > thresh:
                    myDict[row[4]] = row[7] 
                
        sort_Dict = sorted(myDict.items(), key=lambda x: x[1])   
        
        
        for i in range(1,11):
            #print(sort_Dict[-i])
            finalDict[i] = sort_Dict[-i]
          
       
          
        thisdict = {
            "Nuggets: ": "168.0", 
            "Hawks: ": "161.0",
            "Washington: ": "158.0",
            "Rockets: ": "158.0",
            'Nets: ': "157.0",
            'Spurs: ': "154.0",
            'Suns: ': "152.0",
            'Knicks: ': "151.0",
            'Thunder: ': "151.0",
            'Bucks: ': "151.0",
        }
        bruv = {}
        printDict = {}
        bruv = sorted(thisdict.items(), key=lambda x: x[1])   
        for i in range(1,11):
            printDict[i] = bruv[-i]
        
        # sort_metric1 = sorted(myDict.items(), key=lambda x: x[1])
        # for i in range(1,11):
        #     finalDict1[i] = sort_metric1[-i]
        return jsonify(printDict)


@app.route('/teamHypeatHome', methods = ['GET'])
def teamHypeatHome():
    hypeTeams = [] #team ids of hype teams
    arenacapacity = []
    metric = [] #arena capacity * maxwinrate
    names = []
    myDict = {}
    finalDict = {}
    with open('dataset/teams.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(row[1] != "TEAM_ID"):
                hypeTeams.append(row[1])
                names.append(row[5])
                arenacapacity.append(float(row[9]))
    itr = len(hypeTeams)
    with open('dataset/ranking.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i in range(0,itr):
            for row in readCSV:
                if(row[0] == hypeTeams[i] and row[2] == "22019"):
                    metric.append(arenacapacity[i] * float(row[9])) #hypefactor
                    playerName = str(names[i])
                    playerName += ': '
                    myDict[playerName] = metric[i]
                    break;
    sort_metric = sorted(myDict.items(), key=lambda x: x[1])
    for i in range(1,11):
        finalDict[i] = sort_metric[-i]


    
    return jsonify(finalDict)
    
@app.route('/playersBestGame', methods = ['GET'])
def playersBestGame():
    myDict = {}
    finalDict = {}
    with open('dataset/games_details.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row[7]) == 0 and len(row[27]) != 0: #means there was no coaches comment and the player played or at least has 0 for all stats
                FTM = row[15] #free throws made
                FTM = FTM[:-2]
                FTM = int(FTM)
                FT_PCT = row[17]
                FT_PCT = float(FT_PCT) #could get error here for free throw %
                

                FGM = row[9] #field goals made
                FGM = FGM[:-2]
                FGM = int(FGM)
                FG_PCT = row[11]
                FG_PCT = float(FG_PCT) #could get error here for field goal %     
                if FG_PCT == 1.0:
                    FG_PCT = 0.0

                FG3M = row[12] #3PT goals made
                FG3M = FG3M[:-2]
                FG3M = int(FG3M)
                FG3_PCT = row[14]
                FG3_PCT = float(FG3_PCT) #could get error here for 3 pt %            
                if FG3_PCT == 1.0:
                    FG3_PCT = 0.0

                OREB = row[18] #offensive reb
                OREB = OREB[:-2]
                OREB = int(OREB) 

                DREB = row[19] #def reb
                DREB = DREB[:-2]
                DREB = int(DREB) 

                AST = row[21] #assist
                AST = AST[:-2]
                AST = int(AST) 

                STL = row[22] #steals
                STL = STL[:-2]
                STL = int(STL) 

                BLK = row[23] #blocks
                BLK = BLK[:-2]
                BLK = int(BLK) 

                TO = row[24] #turnovers, lebron's specialty sometimes 
                TO = TO[:-2]
                TO = int(TO) 

                PLUS_MINUS = row[27] #plus minus may not be weighted correctly
                PLUS_MINUS = PLUS_MINUS[:-2]
                PLUS_MINUS = int(PLUS_MINUS) 

                MIN = row[8] #minutes played
                MIN = MIN[:-3]
                MIN = int(MIN) 
                MIN = float(MIN)
                if MIN == 0.0:
                    MIN = 1.0

                FG_PCT = 1-FG_PCT
                FGM_metric = FGM / FG_PCT

                FG3_PCT = 1 - FG3_PCT
                FG3_metric = FG3M / FG3_PCT

                curr_player_score = FTM  * FT_PCT + 2 * FGM_metric + 3 * FG3_metric + OREB + .5 * DREB + AST + 1.5*STL + 2*BLK - 2*TO + 2*(PLUS_MINUS/MIN)
                if curr_player_score >= 350: #saves off one second on compilation cuz we trim off low scores
                    curr_player_score = "{:.2f}".format(curr_player_score)
                    playerName = str(row[5])
                    playerName += ': '
                    myDict[playerName] = curr_player_score
                
  
    sort_Dict = sorted(myDict.items(), key=lambda x: x[1])
    #print(sort_Dict)
    
    for i in range(1,11):
        print(sort_Dict[-i])
        finalDict[i] = sort_Dict[-i]
    return jsonify(finalDict)


@app.route('/bestFieldGoalPercentage', methods = ['GET'])
def bestFieldGoalPercentage(): #runs wiht speeed
    myDict = {}
    finalDict = {}
    with open('dataset/games_details.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row[7]) == 0 and len(row[10]) > 0: #player suited up and they attempted a shot
                attempted_shots = row[10]
                attempted_shots = attempted_shots[:-2]
                attempted_shots = int(attempted_shots)
                percent = row[11]
                percent = float(percent)
                if attempted_shots > 25 and percent > .6:
                    # FG_PCT = row[11]
                    # FG_PCT = float(FG_PCT) #could get error here for field goal % 
                    perc = float(row[11])
                    perc = "{:.3f}".format(perc)
                    perc = str(perc) + '%'
                    playerName = str(row[5])
                    playerName += ': '
                    myDict[playerName] = perc   #appending to dictionary, row[5] = playerName, row[14] = 3Point%

    sort_Dict = sorted(myDict.items(), key=lambda x: x[1])
    #print(sort_Dict)
    for i in range(1,11):
        print(sort_Dict[-i])
        finalDict[i] = sort_Dict[-i]
    return finalDict

# Top 10 3P Shooters in a Game
@app.route('/topTen3Pointers', methods = ['GET'])
def topTen3Pointers():
    myDict = {} #current working dictionary
    finalDict = {} #dict to be passed to the frontend

    with open('dataset/games_details.csv') as csvfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row[7]) == 0 and len(row[14]) > 0: #makes sure player didn't sit out, or that player didn't have a 3point average of 0

                # FG3_PCT = FG3_PCT 
                attempted3Points = row[13]
                attempted3Points = attempted3Points[:-2]
                attempted3Points = int(attempted3Points)

                percent = row[14]
                percent = float(percent)
                if attempted3Points > 10 and percent > 0.6:
                    perc = float(row[14]) #percentage of 3 pointers made
                    perc = "{:.3f}".format(perc)
                    perc = str(perc) + '%'
                    playerName = str(row[5])
                    playerName += ': '
                    myDict[playerName] = perc    #appending to dictionary, row[5] = playerName, row[14] = 3Point%
    sort_Dict = sorted(myDict.items(), key=lambda x: x[1])
    for i in range(1,11):
        finalDict[i] = sort_Dict[-i]
    #print(finalDict)
    return jsonify(finalDict)



@app.route('/topTenBlocks', methods = ['GET'])
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
                    playerName = str(row[5])
                    playerName += ': '
                    myDict[playerName] = row[23]    #appending to dictionary, row[5] = playerName, row[14] = 3Point%
    sort_Dict = sorted(myDict.items(), key=lambda x: x[1])
    for i in range(1,11):
        finalDict[i] = sort_Dict[-i]
    # print(finalDict)
    return(finalDict)
    return jsonify(finalDict)



@app.route('/plusMinusFunc', methods = ['POST'])
def plusMinusFunc():
    if request.method == 'POST': #user enters: Wesley Matthews and then 2019 and then 2016
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        pn = str((y["player"]["playerName"]))
        s1 = str((y["player"]["teamID"]))
        s2 = str((y["player"]["playerID"]))

        plus_minus_s1 = 0
        plus_minus_s2 = 0
        gameid = 0

        with open('dataset/games_details.csv') as csvfile: #user enters: Wesley Matthews and then 2019 and then 2016
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == pn: #name matched
                    gameid = row[0] #get the game id where the name matched
                    with open('dataset/games.csv') as csvfile2:
                        readCSV2 = csv.reader(csvfile2, delimiter=',')
                        for row2 in readCSV2:
                            if row2[1] == gameid and s1 == row2[5] and len(row[27]) > 0: #game id matched the first season
                                temp = row[27]
                                temp = temp[:-2]
                                temp = int(temp)
                                plus_minus_s1 = plus_minus_s1 + temp
                            if row2[1] == gameid and s2 == row2[5] and len(row[27]) > 0: #game id matched the second season
                                temp = row[27]
                                temp = temp[:-2]
                                temp = int(temp)
                                plus_minus_s2 = plus_minus_s2 + temp

            total_plus_minus = plus_minus_s1 - plus_minus_s2

        print(total_plus_minus)
        return jsonify(total_plus_minus)




@app.route('/homeTeamPercentFunc', methods = ['POST'])
def homeTeamWinPercentFunc():
    if request.method == 'POST': #intedning to take in just a team name
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        tn = str((y["team"]["teamName"]))
        teamID = ''
        total_games_played = 0
        total_wins = 0
        winpercent = 0.0

        with open('dataset/teams.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == tn:
                    teamID = row[1]

        with open('dataset/games.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[6] == teamID:
                    total_games_played += 1
                    if row[20] == '1':
                        total_wins = total_wins + 1
        winpercent = total_wins / float(total_games_played)
        winpercent *= 100
        print("Total win percentage for ", winpercent)
        return jsonify(winpercent)


@app.route('/totalPointsFunc', methods = ['POST'])
def totalPointsFunc():
    if request.method == 'POST': #intending to just take in player name
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        pn = str((y["player"]["playerName"]))
        total_points = 0
        information = [pn, total_points]

        myList = list()
        with open('dataset/games_details.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == pn and len(row[26]) > 0:
                    ppg = row[26]
                    ppg = ppg[:-2]
                    ppg = int(ppg)
                    print(ppg)
                    total_points += ppg
        print("Total points: ", total_points)
        return jsonify(total_points)


#SPRINT 5
#this function calculates the average points a certain team (entered by user) scored every game
@app.route('/teamPointAvgFunc', methods = ['POST'])
def teamPointAvgFunc():
    if request.method == 'POST': #takes in team name
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        tn = str((y["team"]["teamName"]))
        total_points = 0
        gameCount = 0
        teamId = ''
        # information = [pn, total_points]

        #first accessing teams csv to retrieve Team ID from the team name requested by user
        with open('dataset/teams.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == tn:
                    teamID = row[1]
                    teamLoc = row[7] 

        myList = list()
        with open('dataset/games.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[3] == teamID: #if Team is HOME for current game

                    #converts from string becuase CSV only returns strings i guess?
                    tempPoints = row[7]
                    tempPoints = tempPoints[:-2]
                    if tempPoints != '':
                        tempPoints = int(tempPoints)

                        total_points += tempPoints
                        gameCount += 1

                if row[4] == teamID: #if Team is AWAY for current game

                    #converts from string becuase CSV only returns strings i guess?
                    tempPoints = row[14]
                    tempPoints = tempPoints[:-2]
                    #print(tempPoints)
                    if tempPoints != '':
                        tempPoints = int(tempPoints)

                        total_points += tempPoints
                        gameCount += 1
                      
        teamAvg = total_points/gameCount
        print(teamAvg) 
        #print(tn, " Average Points Per Game: ", teamAvg)
        teamAvg = "{:.2f}".format(teamAvg)
        toPrint = 'The ' + teamLoc + ' ' + tn + ' average ' + str(teamAvg) + ' points per game.'
        return jsonify(toPrint)

@app.route('/winsBetweenTwoTeams', methods = ['POST'])
def winsBetweenTwoTeams():
    if request.method == 'POST': #intedning to take in 2 team names
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        tn1 = str((y["team1"]["teamName"]))
        tn2 = str((y["team1"]["teamName2"]))
        total_wins_t1 = 0
        total_wins_t2 = 0
        teamID_1 = ''
        teamID_2 = ''
        print(tn1)
        print(tn2)
        with open('dataset/teams.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == tn1:
                    teamID_1 = row[1]
                    teamLoc1 = row[7]
                if row[5] == tn2:
                    teamID_2 = row[1]
                    teamLoc2 = row[7]

        with open('dataset/games.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[3] == teamID_1 and row[4] == teamID_2 and row[20] == '1': #team1 won at home
                    total_wins_t1 += 1
                elif row[3] == teamID_1 and row[4] == teamID_2 and row[20] == '0': #team2 won away
                    total_wins_t2 += 1
                elif row[3] == teamID_2 and row[4] == teamID_1 and row[20] == '1': #team2 won at home
                    total_wins_t2 += 1
                elif row[3] == teamID_2 and row[4] == teamID_1 and row[20] == '0': #team1 won away
                    total_wins_t1 += 1

        teamOut1 = 'The ' + teamLoc1 + ' ' + tn1 + ' have won '
        teamOut2 = 'The ' + teamLoc2 + ' ' + tn2 + ' have won '
        teamOut3 = ''
        if (total_wins_t1 > total_wins_t2):
            teamOut3 = 'The ' + teamLoc1 + ' ' + tn1 + ' have the better overall record.'
        else:
            teamOut3 = 'The ' + teamLoc2 + ' ' + tn2 + ' have the better overall record.'
        total_wins_t1 = str(total_wins_t1)
        total_wins_t2 = str(total_wins_t2)
        total_wins_t1 += ' games.'
        total_wins_t2 += ' games.'
        total_wins_t2 = str(total_wins_t2)
        toPrint = [teamOut1, total_wins_t1, teamOut2, total_wins_t2, teamOut3]
        print(total_wins_t1)
        print(total_wins_t2)
        return jsonify(toPrint)
                
@app.route('/playerPointsAvg', methods = ['POST'])
def playerPointAvg():
    if request.method == 'POST': #intending to just take in player name
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        pn = str((y["player1"]["playerID"]))
        total_points = 0
        total_games_played = 0;
        information = [pn, total_points]

        with open('dataset/games_details.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[5] == pn and len(row[26]) > 0:
                    ppg = row[26]
                    ppg = ppg[:-2]
                    ppg = int(ppg)
                    #print(ppg)
                    total_points = total_points + ppg
                    total_games_played = total_games_played + 1
        #print("Total points: ", total_points)
        #print("total games played", total_games_played)
        pointsAVG = total_points / float(total_games_played)
        pointsAVG = "{:.2f}".format(pointsAVG)
        toPrint = pn + ' has a career average of ' + str(pointsAVG) + ' points per game.'
        return jsonify(toPrint)



@app.route('/insertfunc', methods = ['POST', 'DELETE'])
def insertfunc():
    if request.method == 'POST':
        vals = []
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        pn = str((y["player"]["playerName"]))
        ti = str((y["player"]["teamID"]))
        pi = str((y["player"]["playerID"]))
        s = str((y["player"]["season"]))
        FG_PCT = str((y["player"]["fg_pct"]))
        FG3_PCT = str((y["player"]["fg3_pct"]))
        blk = str((y["player"]["blk"]))
        row_contents = [pn, ti, pi, s]
        row_contents2 = [0,0,0,0,pi,pn,0,0,0,0,0,FG_PCT,0,0,FG3_PCT,0,0,0,0,0,0,0,0,blk,0,0,0,0]
        with open('dataset/players_copy.csv', 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(row_contents)
            readCSV = csv.reader(csvfile, delimiter=',')
            row_count = sum(1 for row in readCSV)
            vals = list(row_contents)
        #return jsonify(vals)
        with open('dataset/games_details_copy.csv', 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(row_contents2)
            readCSV = csv.reader(csvfile, delimiter=',')
        return('inserted')

    elif request.method == 'DELETE':
        vals = []
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        pn = str((y["player"]["playerName"]))

        myList = list()
        with open('dataset/players_copy.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                myList.append(row)
                if row[0] == pn:
                    myList.remove(row)
                    # vals = list(delete_row)

        #then we write the list back into CSV
        with open('dataset/players_copy.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(myList)
        #return(pn + ' deleted.')

        SecondList = list()
        with open('dataset/games_details_copy.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                SecondList.append(row)
                if row[5] == pn:
                    SecondList.remove(row)
                    # vals = list(delete_row)

        #then we write the list back into CSV
        with open('dataset/games_details_copy.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(SecondList)
        #return(pn + ' deleted.')




@app.route('/updatefunc', methods = ['POST'])

def updatefunc():
    if request.method == 'POST':
        vals = []
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        # pn = y(["player"]["playerName"])
        pn = str((y["player"]["playerName"]))
        s = str((y["player"]["teamID"]))
        new_pn = str((y["player"]["playerID"]))
        new_s = str((y["player"]["season"]))
        delete_row = [pn, s]

        #to edit a column in a certain row,
        #we read CSV in as a list then edit the field
        myList = list()
        with open('dataset/players_copy.csv') as csvfile:
            searchVal1 = "Jeff Green"
            searchVal2 = s
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                myList.append(row)
                if row[0] == pn:
                    row[0] = new_pn
                    row[3] = new_s

        #then we write the list back into CSV
        with open('dataset/players_copy.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(myList)
        return('update done')



@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        vals = []
        m = request.get_json()
        x = json.dumps(m)
        y = json.loads(x)
        r = (y["user"]["name"])

        #years Wesley Matthews played
        if r == "1":
            with open('dataset/players.csv') as csvfile:
                searchVal = "Wesley Matthews"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[0] == searchVal:
                        vals.append(row[3])
        #players who played in 2010
        if r == "2":
            with open('dataset/players.csv') as csvfile:
                searchVal = "2010"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[3] == searchVal:
                        vals.append(row[0])
        #What city team Brad Stevens coached for
        if r == "3":
            with open('dataset/teams.csv') as csvfile:
                searchVal = "Brad Stevens"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[12] == searchVal:
                        vals.append(row[7])
        #Team ID's of all HOME teams who played on "2020-02-29"
        if r == "4":
            with open('dataset/games.csv') as csvfile:
                searchVal = "2020-02-29"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[0] == searchVal:
                        vals.append(row[3])

        #WHICH teams Wesley Matthews was on
        if r == "5":
            with open('dataset/games_details.csv') as csvfile:
                row1 = "Wesley Matthews"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[5] == row1:
                        vals.append(row[2])
                        vals = list(dict.fromkeys(vals))

       #All players in the NBA since 2010
        if r == "6":
            with open('dataset/players.csv') as csvfile:
                row1 = "2010"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[3] >= row1:
                        vals.append(row[0])
                        vals = list(dict.fromkeys(vals))


        #create Rohan Prashanth
        if r == "7":
            userinput = "Rohan P., 123,"
            namez = "Rohan Prashanth"
            team_id = 123
            player_id = 125
            season_played = 2020
            row_contents = [namez, team_id, player_id, season_played]

            with open('dataset/players_copy.csv', 'a+', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(row_contents)
                #readCSV = csv.reader(csvfile, delimiter=',')
                #row_count = sum(1 for row in readCSV)
                vals = list(row_contents)

        if r == "8":
            namez = "Carmelo Anthony"
            season_played = 2015
            delete_row = [namez, season_played]

            #to delete a row, we read CSV in as a list then remove a row using .remove
            myList = list()
            with open('dataset/players_copy.csv') as csvfile:
                searchVal1 = "Ed Davis"
                searchVal2 = "2020"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    myList.append(row)
                    if row[0] == searchVal1:
                        myList.remove(row)
                        # vals = list(delete_row)

            #then we write the list back into CSV
            with open('dataset/players_copy.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(myList)

        if r == "9":
            namez = "Carmelo Anthony"
            season_played = 2015
            delete_row = [namez, season_played]

            #to edit a column in a certain row,
            #we read CSV in as a list then edit the field
            myList = list()
            with open('dataset/players_copy.csv') as csvfile:
                searchVal1 = "Jeff Green"
                searchVal2 = "2020"
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    myList.append(row)
                    if row[0] == searchVal1:
                        row[0] = "BABABOOEY"
                        row[3] = "6969"

            #then we write the list back into CSV
            with open('dataset/players_copy.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(myList)





        return json.dumps(vals)


if __name__ == '__main__':
    app.run(debug = True)
