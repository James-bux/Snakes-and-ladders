import time
import os

y0 = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"]
y1 = ["11","12","13","14","15","16","17","18","19","20"]
ylist = [y0, y1]

def printTable():
  for i in ylist:
    printY = ""
    for y in i:
      printY += y
    print(printY)

while True:
  
  os.system('clear')
  printTable()
