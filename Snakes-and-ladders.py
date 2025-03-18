import time
import random
import os

players = input("How many people are playing the game?")

y0 = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"]
y1 = ["11","12","13","14","15","16","17","18","19","20"]
y2 = ["21","22","23","24","25","26","27","28","29","30"]
y3 = ["31","32","33","34","35","36","37","38","39","40"]
y4 = ["41","42","43","44","45","46","47","48","49","50"]
y5 = ["51","52","53","54","55","56","57","58","59","60"]
y6 = ["61","62","63","64","65","66","67","68","69","70"]
y7 = ["71","72","73","74","75","76","77","78","79","80"]
y8 = ["81","82","83","84","85","86","87","88","89","90"]
y9 = ["91","92","93","94","95","96","97","98","99","Fi"]

ylist = [y0, y1]

def printTable():
  for i in ylist:
    printY = ""
    for y in i:
      printY += y
      printY += "  "
    print(printY)
  
def gen_lads_and_snak():
  numlads = randint(3,7)
  numsnakes = randint(3,7)
  for i in range(numlads):

def playerMove():
  for i in range(1,players):
    
  
while True:
  
  os.system('clear')
  printTable()
