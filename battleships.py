# Battleship
import random
import os
import sys


def AI_pick_shooting_coordinate():
    '''
    coord = []
    first_hit = []
    second_hit = []
    acceptable_target_coords = []
    if first_hit == []:
        # if there are no hits yet, then just shoot at a random coordinate.
        x, y = random.randrange(0, 9)
        coord.append(x, y)

    elif first_hit != [] and second_hit == []:
        # first hit is not empty, but we have no second_hit yet, pick a coord near first_hit
        acceptable_target_coords.append(first hit[0]-1, first_hit[1])
        acceptable_target_coords.append(first hit[0]+1, first_hit[1])
        acceptable_target_coords.append(first hit[0], first_hit[1]-1)
        acceptable_target_coords.append(first hit[0], first_hit[1]+1)
        for x, y in acceptable_target_coords:
            if x, y < 0 or x, y > 9:
    '''         


def menuKeys(key):
    pass
''' if key == "q":
        sys.exit(0)
    elif key == "n":
        return False  # You can't return break!!!
'''
def init():
    global player1Turn
    global player1Name
    player1Name = input("Player 1's name: ")
    global player2Name
    player2Name = input("Player 2's name: ")
    global currentEvent
    currentEvent = ""
    global player1Board
    player1Board = []
    global player2Board
    player2Board = []
    global player1Ship5
    player1Ship5 = []
    global player1Ship4
    player1Ship4 = []
    global player1Ship3
    player1Ship3 = []
    global player2Ship5
    player2Ship5 = []
    global player2Ship4
    player2Ship4 = []
    global player2Ship3
    player2Ship3 = []
    global coord
    coord = []
    for i in range(0, 10):
        player1Board.append(["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"])
    for i in range(0, 10):
        player2Board.append(["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"])

def inputAndCheck():
    x=""
    y=""
    validCharList="abcdefghij"
    coord=[]
    while True:
        x=input("input x coordinate (A-J): ")
        x=x.lower()
        menuKeys(x)
        if x in validCharList:
            x=validCharList.index(x)
            break
        else:
            print("invalid coordinate, x needs to be a letter between (A-J): ")
            continue
    while True:
        y=input("input y coordinate (1-10): ")
        menuKeys(y)
        try:
            y=int(y)-1
            if y<0 or y>9:
                raise ValueError
            else:
                break
        except ValueError:
            print("invalid coordinate, y needs to be a number between (1-10): ")
            continue
    coord.append(y)
    coord.append(x)
    return coord
def showBoard(player1Board, player2Board, whoseTurn):
    currentPlayerBoard=[]
    enemyPlayerBoard=[]
    currentPlayerName=""
    currentLine=""
    if whoseTurn:
        currentPlayerName=player1Name
        currentPlayerBoard=player1Board
        enemyPlayerBoard=player2Board
    else:
        currentPlayerName=player2Name
        currentPlayerBoard=player2Board
        enemyPlayerBoard=player1Board


    #"clear" the screen and print a header
    os.system('clear')
    print(currentPlayerName + "'s turn")
    print("=================================================", "\n")
    print("   Player's ships             Previous shots")
    print("   A B C D E F G H I J        A B C D E F G H I J")
    
    for i in range(0,10):
        currentLine=""
        #print the player board on the left
        if i<9:  
            print(i+1, sep=" ", end="  ")
        else:
            print(i+1, sep=" ", end=" ")
        for j in range(0,10):
            print(currentPlayerBoard[i][j], sep=" ", end=" ", flush=True)
        
        #add spacing between the two boards
        print("   ", sep=" ", end=" ")
        
        #print the enemy board on the right
        if i<9:  
            print(i+1, sep=" ", end="  ")
        else:
            print(i+1, sep=" ", end=" ")
        for j in range(0,10):
            currentLine=currentLine+str(enemyPlayerBoard[i][j])+" "
        print(currentLine.replace("S", "~"))
        #the following seems to be needed to print in the following line... ("\n" skips a line)

def shot(whoseTurn):
    global player1Board
    global player2Board
    shot=[]
    
    while True:
        shot=inputAndCheck()
        shotX=int(shot[0])
        shotY=int(shot[1])

        if whoseTurn and player2Board[shotX][shotY] == "S":
            player2Board[shotX][shotY]="O"
            break
        elif whoseTurn and player2Board[shotX][shotY] == "~":
            player2Board[shotX][shotY]="X"
            break
        elif whoseTurn and player2Board[shotX][shotY] == "X" or player2Board[shotX][shotY] == "O":
            print("coordinate already shot, choose another one!")
            continue
        
        if whoseTurn is False and player1Board[shotX][shotY] == "S":
            player1Board[shotX][shotY]="O"
            break
        elif whoseTurn is False and player1Board[shotX][shotY] == "~":
            player1Board[shotX][shotY]="X"
            break
        elif whoseTurn is False and player1Board[shotX][shotY] == "X" or player1Board[shotX][shotY] == "O":
            print("coordinate already shot, choose another one!")
            continue

def setShip(length):
    shipList = []
    while True:
        print("Please input starting coordinates for a", length, "long ship.")
        firstPos = inputAndCheck()  # e.g.: [1,1]
        print("Please input ending coordinates for a", length, "long ship.")
        lastPos = inputAndCheck()  # e.g.: [1,5]
        while True: #input ship coordinate and check if valid (either x or y of the beginning and end must match and their distance can't be more than the ship's length)
            if firstPos[0] == lastPos[0]: #Check if y coords are the same
                if firstPos[1] > lastPos[1]: #set which x coord is smaller
                    smallerValue = lastPos[1]
                    for i in range(0, abs(firstPos[1] - lastPos[1])+1):
                        shipList.append([firstPos[0], smallerValue + i])
                elif firstPos[1] < lastPos[1]:
                    smallerValue = firstPos[1]
                    for i in range(0, abs(firstPos[1] - lastPos[1])+1):
                        shipList.append([firstPos[0], smallerValue + i])
                break

            elif firstPos[1] == lastPos[1]: #same as above only the other way around.
                if firstPos[0] > lastPos[0]:
                    smallerValue = lastPos[0]
                    for i in range(0, abs(firstPos[0] - lastPos[0])+1):
                        shipList.append([smallerValue + i, firstPos[1]])
                elif firstPos[0] < lastPos[0]:
                    smallerValue = firstPos[0]
                    for i in range(0, abs(firstPos[0] - lastPos[0])+1):
                        shipList.append([smallerValue + i, firstPos[1]])
                break
            else:
                print("Invalid coordinates!")
                shipList=[]
                continue

        if int(len(shipList)) != length:
            print("Invalid coordinates!")
            shipList=[]
            continue

        if player1Turn:
            for i in range(0, length):
                if player1Board[shipList[i][0]][shipList[i][1]] == "S":
                    shipList=[]
                    print("Ship obstructed, try placing elsewhere")
                    break
            if shipList==[]:
                continue
            else:
                break

        elif not player1Turn:
            for i in range(0, length):
                if player2Board[shipList[i][0]][shipList[i][1]] == "S":
                    shipList=[]
                    print("Ship obstructed, try placing elsewhere")
                    break
            if shipList==[]:
                continue
            else:
                break                      

    if player1Turn:
        for i in range(0, length):
            player1Board[shipList[i][0]][shipList[i][1]] = "S"
    else:
        for i in range(0, length):
            player2Board[shipList[i][0]][shipList[i][1]] = "S"

    return shipList

def winStateCheck():
    p1Ships=0
    p2Ships=0
    for i in range(0,10):
        for j in range(0,10):
            if player2Board[i][j]=="S":
                p1Ships+=1
            if player1Board[i][j]=="S":
                p2Ships+=1
    if p1Ships==0:
        print("Game over,", player2Name, "wins!")
        return True
    if p2Ships==0:
        print("Game over,", player1Name, "wins!")
        return True

def shipSunkCheck(shipList, whoseShip): #whoseShip true for p1, false for p2
    shipDamage=0
    for i in range(0, len(shipList)): #check each set of coords the ship has e.g.: each [x,y]
        if whoseShip and player1Board[shipList[i][0]][shipList[i][1]]=="O":
            shipDamage+=1
            if shipDamage==len(shipList):
                for j in range(0,len(shipList)):
                    player1Board[shipList[j][0]][shipList[j][1]]="+"
        if whoseShip is False and player2Board[shipList[i][0]][shipList[i][1]]=="O":
            shipDamage+=1
            if shipDamage==len(shipList):
                for j in range(0,len(shipList)):
                    player2Board[shipList[j][0]][shipList[j][1]]="+"


while True:
    init()
    player1Turn = True	
    showBoard(player1Board, player2Board, player1Turn)
    print("Press any key to start deploying ships for", player1Name)
    player1Ship3=setShip(3)
    showBoard(player1Board, player2Board, player1Turn)
    player1Ship4=setShip(4)
    showBoard(player1Board, player2Board, player1Turn)
    player1Ship5=setShip(5)
    showBoard(player1Board, player2Board, player1Turn)
    input("Ships deployed, press any key to deploy for next player...")
    player1Turn = False
    showBoard(player1Board, player2Board, player1Turn)
    print("Press any key to start deploying ships for", player2Name)
    player2Ship3=setShip(3)
    showBoard(player1Board, player2Board, player1Turn)
    player2Ship4=setShip(4)
    showBoard(player1Board, player2Board, player1Turn)
    player2Ship5=setShip(5)
    showBoard(player1Board, player2Board, player1Turn)
    player1Turn = random.choice((True, False))
    input("All ships deployed, press a key to start. Random player goes first.")
    while True:
        showBoard(player1Board, player2Board, player1Turn)
        shot(player1Turn)
        shipSunkCheck(player1Ship3, player1Turn)
        shipSunkCheck(player1Ship4, player1Turn)
        shipSunkCheck(player1Ship5, player1Turn)
        shipSunkCheck(player2Ship3, player1Turn)
        shipSunkCheck(player2Ship4, player1Turn)
        shipSunkCheck(player2Ship5, player1Turn)
        showBoard(player1Board, player2Board, player1Turn)
        if winStateCheck():
            input("Press any key to start a new game")
            break
        #winStateCheck(player1Turn)
        input("Press any key to continue...")
        player1Turn = not player1Turn
    
