import time
import random
import os


AmPlayers = int(input("How many people are playing the game?"))
players = []
i = 0
for x in range(1,AmPlayers):
  i += 1
  players += i
y0 = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"]
y1 = ["11","12","13","14","15","16","17","18","19","20"]
y2 = ["21","22","23","24","25","26","27","28","29","30"]
y3 = ["31","32","33","34","35","36","37","38","39","40"]
y4 = ["41","42","43","44","45","46","47","48","49","50"]
y5 = ["51","52","53","54","55","56","57","58","59","60"]
y6 = ["61","62","63","64","65","66","67","68","69","70"]
y7 = ["71","72","73","74","75","76","77","78","79","80"]
y8 = ["81","82","83","84","85","86","87","88","89","90"]
y9 = ["91","92","93","94","95","96","97","98","99","100"]

ylist = [y0, y1]

def printTable():
  for i in ylist:
    printY = ""
    for y in i:
      printY += y
      printY += "  "
    print(printY)

def gen_lads():
  numlads = random.randint(3,7)
  for i in range(numlads):
    ladders = open("ladders.txt", "w")
    ladstart = random.randint(1,100)
    ladend = random.randint(ladstart, 100)
    ladders.write(str(ladstart)+","+str(ladend)+"\n")
  ladders.close()
  return(numlads)
def gen_snakes():
  numsnakes = random.randint(3,7)
  for i in range(numsnakes):
    snakes = open("snakes.txt", "w")
    snakestart = random.randint(1,100)
    snakeend = random.randint(1, snakestart)
    snakes.write(str(snakestart)+","+str(snakeend)+"\n")
  snakes.close()
  return(numsnakes)
  
  

def checksnakes(playloc, numsnakes):
  snakes = open("snakes.txt", "r")
  for i in range(numsnakes):
    snakeline = snakes.readlines(1)
    snakepos = snakeline.split(,)
    if playloc == snakepos[1]:
      playloc = snakepos[2]
      print("you slid down a snake to"+str(snakepos[2]))
      break
    return(playloc)
    

def RTD():
  diceRoll = random.randint(1,6)
  return diceRoll

def playerMove():
  for i in range(1,AmPlayers):
    RTD()  

while True:
  
  os.system('clear')
  printTable()
