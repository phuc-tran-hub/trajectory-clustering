# Name: Phuc Tran
# Date: January 5th, 2022
# Title: OPTICSsimulation.c
# Description: in the simulation, 

# Libraries
import matplotlib.pyplot as plt
import numpy as np
from TRACLUSdistance import traclusDistance
from line import Line
from OPTICS import opticsclustering

# setting the plot's size
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.axis([0, 20, 0, 20])

# making coordinates (x0, y0, x1, y1)
# generated ten line segments
coords = np.round(np.random.rand(3, 4)*20)
print(coords)

coordsObjList = []

lineID = 1

for line in coords:
   # extracting the x coordinates and y coordinates to graph lines
   xCoords = [line[0], line[2]]
   yCoords = [line[1], line[3]]

   # extracting coordinates and saving onto a line segment array
   newLine = []
   newLine.append([xCoords[0], yCoords[0]])
   newLine.append([xCoords[1], yCoords[1]])
   
   newSeg = Line(lineID, newLine)
   lineID = lineID + 1 
   coordsObjList.append(newSeg)


# setting parameters:
# DL is the list of line segments 
# eps is the threshold distance for line segments
# minLns is the minimum line segments for a group
DL = np.copy(coordsObjList)
eps = 2
minLns = 1
newDL = opticsclustering(DL, eps, minLns)

for line in newDL:
    print("line's ID: " + str(line.lineID) + "\t line's clusterID: " + str(line.clusterID) + "\t \t line's lineSeg: " + str(line.lineSeg))
    xCoords = [line.lineSeg[0][0], line.lineSeg[1][0]]
    yCoords = [line.lineSeg[0][1], line.lineSeg[1][1]]
    # displaying the line segment
    plt.plot(xCoords, yCoords, label = str(line.lineID))

plt.legend()
plt.show()