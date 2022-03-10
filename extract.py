# Name: Phuc Tran
# Date: March 1st, 2022
# Title: preprocess.c
# Description: pulling out data from a AIS csv file to store into line segments

from preprocess import preprocess
import matplotlib.pyplot as plt
import numpy as np
from line import Line
from OPTICS import opticsclustering

shipObjectList = preprocess('./trajectory-clustering/aisdk_20170701.csv', 5000)

# setting the plot's size
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.axis([0, 100, 0, 100])

coordsObjList = []
lineID = 1

# making the most recent line coordinates out of every ships
# generated ten line segments
for shipObject in shipObjectList:
    if len(shipObject.positionList) > 3:
        secondLatestPosition = shipObject.positionList[len(shipObject.positionList) - 2]
        LatestPosition = shipObject.positionList[len(shipObject.positionList) - 1]

        # extracting the x coordinates and y coordinates to graph lines
        xCoords = [secondLatestPosition[1], LatestPosition[1]]
        yCoords = [secondLatestPosition[2], LatestPosition[2]]

        # extracting coordinates and saving onto a line segment array
        newLine = []
        newLine.append([xCoords[0], yCoords[0]])
        newLine.append([xCoords[1], yCoords[1]])

        newSeg = Line(lineID, newLine)
        lineID = lineID + 1 
        coordsObjList.append(newSeg)
        print(coordsObjList)


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