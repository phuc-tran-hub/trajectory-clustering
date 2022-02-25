# Name: Phuc Tran
# Date: January 5th, 2022
# Title: linesimulation.c
# Description: create a collection of lines and display them onto a screen

# Libraries
import matplotlib.pyplot as plt
import numpy as np
from TRACLUSdistance import traclusDistance

# setting the plot's size
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# making coordinates (x0, y0, x1, y1)
# generated two line segments
# coords = np.round(np.random.rand(2, 4)*20)

coords = np.array([[5, 5, 5, 10],[10, 3, 10, 11]])
# coords = np.array([[10, 3, 10, 11], [5, 5, 5, 10]])

lines = []
linesimulationTests = open("linesimulationTests.txt", 'w')

plt.axis([0, 20, 0, 20])

for line in coords:

   # extracting the x coordinates and y coordinates to graph lines
   xCoords = [line[0], line[2]]
   yCoords = [line[1], line[3]]

   # extracting coordinates and saving onto a line segment array
   newLine = []
   newLine.append([xCoords[0], yCoords[0]])
   newLine.append([xCoords[1], yCoords[1]])
   lines.append(newLine)

   # displaying the line segment
   plt.plot(xCoords, yCoords)

# testing coordinates of each line segment
linesimulationTests.write("line segments: \t" + str(lines) + "\n")

# to test distance function
linesimulationTests.write("TRACLUS distance: \t" + str(traclusDistance(lines[0], lines[1])))

# plotting
plt.show()
linesimulationTests.close()