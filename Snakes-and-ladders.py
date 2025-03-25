import time
import random
import os

AmPlayers = 0
while AmPlayers < 1:
  AmPlayers = input("How many people are playing the game?") #asks how many people are playing the game
  AmPlayers = int(AmPlayers)
players = [] #stores the players
playerPos = [0,0,0,0,0,0,0] #stores the players position
i = 0
for x in range(1,int(AmPlayers)):
  i += 1
  players.extend(str(i)) #idk what this does it doesnt really work



input("press enter to start")
y0 = ["01","02","03","04","05","06","07","08","09","10"] #big table of the board
y1 = ["20","19","18","17","16","15","14","13","12","11"]
y2 = ["21","22","23","24","25","26","27","28","29","30"]
y3 = ["40","39","38","37","36","35","34","33","32","31"]
y4 = ["41","42","43","44","45","46","47","48","49","50"]
y5 = ["60","59","58","57","56","55","54","53","52","51"]
y6 = ["61","62","63","64","65","66","67","68","69","70"]
y7 = ["80","79","78","77","76","75","74","73","72","71"]
y8 = ["81","82","83","84","85","86","87","88","89","90"]
y9 = ["100","99","98","97","96","95","94","93","92","91"]


ylist = [y9,y8,y7,y6,y5,y4,y3,y2,y1,y0] #construct the board

def checkForPlayerPOS(y): #must i explain this?
  for i in range(0,AmPlayers):
    if playerPos[i] == y:
      return ("P" + str(i+1))
  return str(y)

def printTable(interpolate, player): #prints the table and the players' positions
  for i in ylist:
    if i == y9:
      printY = "" #reset the line
    else:
      printY = " "
    for y in i:
      ConcCurr = str(checkForPlayerPOS(int(y)))
      if i == y0 and not y == "10" and not 'P' in ConcCurr: #checks if the y = the bottom layer
        printY += " " #adds an extra space
      if interpolate == 1 and ('P' + str(player)) in ConcCurr: #icr what interpolate
        printY += y 
        printY += 'P' + str(player+1) #prints the player at the player position
      else:
        printY += ConcCurr
        printY += "| " #cool litle border to show the segments on the board
    print(printY) #print one line

def printList(DaList): #prints the players position for easy reading
  DaPrint = ""
  for i in range(AmPlayers):
    DaPrint += "P"
    DaPrint += str(i + 1)
    DaPrint += ":"
    DaPrint += str(DaList[i])
    DaPrint += "  "
  return DaPrint

def gen_lads(): #i dont need to explain thtis
  numlads = random.randint(7,15)
  ladbottoms = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  ladtops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in range(numlads):
    ladbottoms[i] = random.randint(1,89) #generate the bottom of a ladder on any layer from 0-8
    ladtops[i] = random.randint(ladbottoms[i]+1, 100) #generate the top from bottom to 100
  return numlads, ladbottoms, ladtops #return all the data to be set as variables

def gen_snakes(): #i dont need to explain this either
  numsnakes = random.randint(7,15)
  snakeHeads = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  snakeTails = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in range(numsnakes):
    snakeHeads[i] = random.randint(11,99) # generate the head of a snake from layer 1-9
    snakeTails[i] = random.randint(1,snakeHeads[i]) # generate the tail of the snake from layer0-the snake head
  return numsnakes, snakeHeads, snakeTails #same as the ladders

def checksnakes(player): #checks if the player is on a snake
  for i in range(numsnakes):
    if playerPos[player] == snakeHeads[i]:
      print(str(player + 1) + " has been eaten by a snake")
      time.sleep(1)
      return snakeTails[i]
  return(playerPos[player])

def checklads(player): #checks if the player is on a ladder 
  for i in range(numlads):
    if playerPos[player] == ladbottoms[i]:
      print(str(player + 1) + " has gone up a ladder")
      time.sleep(1)
      return ladtops[i]
  return(playerPos[player])

def RTD(): #roll the dice
  diceRoll = random.randint(1,6)
  return diceRoll

def moveIndvPlayer(player,distance): #move an individual player a given distance
  for i in range(distance):
    playerPos[player] += 1
    os.system('clear')
    printTable(0, player)
    time.sleep(0.2)
  return(playerPos[player])

def playerMove(): #move the players
  for i in range(0,AmPlayers):
    os.system('clear')
    printTable(0,'e')
    print(printList(playerPos))
    print("Player " + str(i+1) + " move:")
    input()
    playerMove = RTD()
    if playerPos[i] + playerMove > 100:
      return "no","0"
    if playerPos[i] + playerMove == 100:
      return "yes",i
    playerPos[i] = moveIndvPlayer(i,playerMove)
    playerPos[i] = checksnakes(i)
    playerPos[i] = checklads(i)
  return "no","0"

snakeinfo = gen_snakes()  #game setup
numsnakes = snakeinfo[0]
snakeHeads = snakeinfo[1]
snakeTails = snakeinfo[2]
ladinfo = gen_lads()
numlads = ladinfo[0]
ladbottoms = ladinfo[1]
ladtops = ladinfo[2]
os.system('clear')
while True: #main game loop
  win = playerMove()
  if win[0] == "yes":
    print("Player " + str(win[1]+1) + " wins!")
    break
