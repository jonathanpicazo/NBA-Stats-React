def UpdateBlocks():
    playerblocks = {
    "Hassan Whiteside": "12.0",
    "JaVale McGee": "12.0",
    "Roy Hibbert": "11.0",
    "Joakim Noah": "11.0",
    "Larry Sanders": "10.0",
    "Anthony Davis": "10.0",
    "Serge Ibaka": "10.0",
    "Andrew Bynum": "10.0",
    "Dikembe Mutombo": "10.0",
    "Calvin Booth": "10.0"
    }
    #receive form from front end(playername,metric)
    try:
        print("Insert player name: ")
        playername = input()
        print("Insert metric amount: ")
        metric = input()
    except EOFError as e:
        print(end="")
    playerblocks.update({playername: metric})
    sort_Dict = sorted(playerblocks.items(), key=lambda x: x[1])
    playerblocks.clear()
    for i in range(1,11):
    	playerblocks[i] = sort_Dict[-i]
    print(playerblocks)

def UpdateTeamPerformance():
    teamperformance = {
    "Nuggets": "168.0",
    "Hawks": "161.0",
    "Rockets": "158.0",
    "Washington": "158.0",
    "Nets": "157.0",
    "Spurs": "154.0",
    "Suns": "152.0",
    "Bucks": "151.0",
    "Thunder": "151.0",
    "Knicks": "151.0",
    }
    #receive form from front end(playername,metric)
    try:
        print("Insert team name: ")
        playername = input()
        print("Insert metric amount: ")
        metric = input()
    except EOFError as e:
        print(end="")
    teamperformance.update({playername: metric})
    sort_Dict = sorted(teamperformance.items(), key=lambda x: x[1])
    teamperformance.clear()
    for i in range(1,11):
    	teamperformance[i] = sort_Dict[-i]
    print(teamperformance)

def Updatethreeptgoal():
    threeptgoal = {
    "Ty Lawson": "0.909",
    "Jodie Meeks": "0.818",
    "Yogi Ferrell": "0.818",
    "Jamal Murray": "0.818",
    "Rodrigue Beaubois": "0.818",
    "Mario Chalmers": "0.769",
    "Zach LaVine": "0.765",
    "Omri Casspi": "0.750",
    "Carmelo Anthony": "0.750",
    "Dorell Wright": "0.750"
    }
    #receive form from front end(playername,metric)
    try:
        print("Insert player name: ")
        playername = input()
        print("Insert metric amount: ")
        metric = input()
    except EOFError as e:
        print(end="")
    threeptgoal.update({playername: metric})
    sort_Dict = sorted(threeptgoal.items(), key=lambda x: x[1])
    threeptgoal.clear()
    for i in range(1,11):
    	threeptgoal[i] = sort_Dict[-i]
    #print(playerblocks)
    print(threeptgoal)
def Updatefg():
    fieldgoal = {
    "Amar'e Stoudemire": "0.741",
    "Paul George": "0.731",
    "Steve Nash": "0.714",
    "Andre Miller": "0.710",
    "Anthony Davis": "0.706",
    "Al Jefferson": "0.704",
    "Vince Carter": "0.704",
    "DeMarcus Cousins": "0.700",
    "Mo Williams": "0.692",
    "Carmelo Anthony": "0.692"
    }
    #receive form from front end(playername,metric)
    try:
        print("Insert player name: ")
        playername = input()
        print("Insert metric amount: ")
        metric = input()
    except EOFError as e:
        print(end="")
    fieldgoal.update({playername: metric})
    sort_Dict = sorted(fieldgoal.items(), key=lambda x: x[1])
    fieldgoal.clear()
    for i in range(1,11):
    	fieldgoal[i] = sort_Dict[-i]
    print(fieldgoal)
def UpdatePlayerPerformance():
    playerperformance = {
    "Klay Thompson": "560.07",
    "Shaquille O'Neal": "498.62",
    "Chandler Parsons": "441.49",
    "Jonas Valanciunas": "425.36",
    "Ty Lawson": "416.41",
    "Seth Curry": "415.57",
    "Tobias Harris": "395.53",
    "Chris Paul": "392.97",
    "Hassan Whiteside": "392.35",
    "Marc Gasol": "390.78"
    }
    #receive form from front end(playername,metric)
    try:
        print("Insert player name: ")
        playername = input()
        print("Insert metric amount: ")
        metric = input()
    except EOFError as e:
        print(end="")
    playerperformance.update({playername: metric})
    sort_Dict = sorted(playerperformance.items(), key=lambda x: x[1])
    playerperformance.clear()
    for i in range(1,11):
    	playerperformance[i] = sort_Dict[-i]
    print(playerperformance)
    
def UpdateTeamHype():
    teamhype =	{
    "Raptors": "15622.2",
    "Bucks": "15225",
    "Lakers": "14923.98",
    "76ers": "13454.05",
    "Clippers": "13380.12",
    "Heat": "13347.60",
    "Nuggets": "13292.90",
    "Celtics": "12943.68",
    "Mavericks": "11846.4",
    "Pacers": "11667.42"
    }
    #receive form from front end(playername,metric)
    try:
        print("Insert team name: ")
        playername = input()
        print("Insert metric amount: ")
        metric = input()
    except EOFError as e:
        print(end="")
    teamhype.update({playername: metric})
    sort_Dict = sorted(teamhype.items(), key=lambda x: x[1])
    teamhype.clear()
    for i in range(1,11):
    	teamhype[i] = sort_Dict[-i]
    print(teamhype)
