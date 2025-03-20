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
  numlads = random.randint(7,15)
  ladders = open("ladders.txt", "w")
  for i in range(numlads):
    ladstart = random.randint(1,100)
    ladend = random.randint(ladstart, 100)
    ladders.write(str(ladstart)+","+str(ladend)+"\n")
  ladders.close()
  return(numlads)
  
numsnakes = random.randint(7,15)
snakeHeads = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
snakeTails = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def gen_snakes():
  for i in range(numsnakes):
    snakeHeads[i] = random.randint(11,99)
    snakeTails[i] = random.randint(1,snakeHeads[i])

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
    ladline = str(ladders.readlines(i))
    ladpos = ladline.split(',')
    if playloc == ladpos[1]:
      playloc = ladpos[2]
      print("you climbed a ladder to"+str(ladpos[2]))
      break
    return(playloc)

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
gen_snakes()
os.system('clear')
while True:
  playerMove()
