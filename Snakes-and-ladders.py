import time
import random
import os

AmPlayers = 0
while AmPlayers < 1:
  AmPlayers = input("How many people are playing the game?")
  AmPlayers = int(AmPlayers)
players = []
playerPos = [0,0,0,0,0,0,0]
i = 0
for x in range(1,int(AmPlayers)):
  i += 1
  players.extend(str(i))



input("press enter to start")
y0 = ["01","02","03","04","05","06","07","08","09","10"]
y1 = ["20","19","18","17","16","15","14","13","12","11"]
y2 = ["21","22","23","24","25","26","27","28","29","30"]
y3 = ["40","39","38","37","36","35","34","33","32","31"]
y4 = ["41","42","43","44","45","46","47","48","49","50"]
y5 = ["60","59","58","57","56","55","54","53","52","51"]
y6 = ["61","62","63","64","65","66","67","68","69","70"]
y7 = ["80","79","78","77","76","75","74","73","72","71"]
y8 = ["81","82","83","84","85","86","87","88","89","90"]
y9 = ["100","99","98","97","96","95","94","93","92","91"]


ylist = [y9,y8,y7,y6,y5,y4,y3,y2,y1,y0]

def checkForPlayerPOS(y):
  for i in range(0,AmPlayers):
    if playerPos[i] == y:
      return ("P" + str(i+1))
  return str(y)

def printTable(interpolate, player):
  for i in ylist:
    if i == y9:
      printY = ""
    else:
      printY = " "
    for y in i:
      ConcCurr = str(checkForPlayerPOS(int(y)))
      if i == y0 and not y == "10" and not 'P' in ConcCurr:
        printY += " "
      if interpolate == 1 and ('P' + str(player)) in ConcCurr:
        printY += y
        printY += 'P' + str(player+1)
      else:
        printY += ConcCurr
        printY += "| "
    print(printY)

def gen_lads():
  numlads = random.randint(7,15)
  ladbottoms = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  ladtops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in range(numsnakes):
    ladbottoms[i] = random.randint(1,99)
    ladtops[i] = random.randint(ladbottoms[i], 100)
  return numlads, ladbottoms, ladtops

def gen_snakes():
  numsnakes = random.randint(7,15)
  snakeHeads = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  snakeTails = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in range(numsnakes):
    snakeHeads[i] = random.randint(11,99)
    snakeTails[i] = random.randint(1,snakeHeads[i])
  return numsnakes, snakeHeads, snakeTails

def checksnakes(player):
  for i in range(numsnakes):
    if playerPos[player] == snakeHeads[i]:
      print(str(player) + " has been eaten by a snake")
      return snakeTails[i]
  return(playerPos[player])
def checklads(playloc, numlads):
  ladders = open("ladders.txt", "r")
  for i in range(numsnakes):
    print(ladbottoms)
  for i in range(numlads):
    if playerPos[player] == ladbottoms[i]:
      print(str(player) + " has climbed a ladder")
      return ladtops[i]
  return(playerPos[player])

def RTD():
  diceRoll = random.randint(1,6)
  return diceRoll

def moveIndvPlayer(player,distance):
  for i in range(distance):
    playerPos[player] += 1
    os.system('clear')
    printTable(0, player)
    time.sleep(0.2)
  return(playerPos[player])

def playerMove():
  for i in range(0,AmPlayers):
    os.system('clear')
    printTable(0,'e')
    print(playerPos)
    print("Player " + str(i+1) + " move:")
    input()
    playerMove = RTD()
    if playerPos[i] + playerMove > 100:
      return
    playerPos[i] = moveIndvPlayer(i,playerMove)
    playerPos[i] = checksnakes(i)
    #playerPos[i] = checklads(playerPos[i])

snakeinfo = gen_snakes()
numsnakes = snakeinfo[0]
snakeHeads = snakeinfo[1]
snakeTails = snakeinfo[2]
ladinfo = gen_lads()
numlads = ladinfo[0]
ladbottoms = ladinfo[1]
ladtops = ladinfo[2]
os.system('clear')
while True:
  playerMove()
