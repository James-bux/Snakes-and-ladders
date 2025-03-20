import time
import random
import os
import re

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
y1 = ["11","12","13","14","15","16","17","18","19","20"]
y2 = ["21","22","23","24","25","26","27","28","29","30"]
y3 = ["31","32","33","34","35","36","37","38","39","40"]
y4 = ["41","42","43","44","45","46","47","48","49","50"]
y5 = ["51","52","53","54","55","56","57","58","59","60"]
y6 = ["61","62","63","64","65","66","67","68","69","70"]
y7 = ["71","72","73","74","75","76","77","78","79","80"]
y8 = ["81","82","83","84","85","86","87","88","89","90"]
y9 = ["91","92","93","94","95","96","97","98","99","100"]

ylist = [y9,y8,y7,y6,y5,y4,y3,y2,y1,y0]

def checkForPlayerPOS(y):
  for i in range(0,AmPlayers):
    if playerPos[i] == y:
      return ("P" + str(i+1))
  return str(y)

def printTable():
  for i in ylist:
    printY = ""
    for y in i:
      ConcCurr = str(checkForPlayerPOS(int(y)))
      printY += ConcCurr
      if i == y0 and not 'P' in ConcCurr:
        printY += " "
      printY += "  "
    print(printY)

def gen_lads():
  numsnakes = random.randint(7,15)
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
  print(snakeHeads)
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

def playerMove():
  for i in range(0,AmPlayers):
    printTable()
    print(playerPos)
    print("Player " + str(i+1) + " move:")
    input()
    playerMove = RTD()
    if playerPos[i] + playerMove > 100:
      return
    playerPos[i] += playerMove
    playerPos[i] = checksnakes(i)
    #playerPos[i] = checklads(playerPos[i])
    input()
    os.system('clear')
snakeinfo = gen_snakes()
numsnakes = snakeinfo[1]
snakeHeads = snakeinfo[2]
snakeTails = snakeinfo[3]
ladinfo = gen_lads()
numlads = ladinfo[1]
ladbottoms = ladinfo[2]
ladtops = ladinfo[3]
os.system('clear')
while True:
  playerMove()
