# Name: Phuc Tran
# Date: January 5th, 2022
# Title: distance.c
# Description: calculate an abstract weighted distance function between two line segments

# Libraries
import numpy as np
import math

'''calculate the distance between two line segments.'''
def distance(line1, line2):
    # the weight of each lines
    wPerpendicular = 0
    wLateral = 1
    wAngle = 1

    print(line1)
    print(line2)

    pDistance = perpendiculardistance(line1, line2)
    latDistance = lateraldistance(line1, line2)
    angDistance = angle(line1, line2)

    # distance equals the weighted parallel distance plus weighted lateral distance plus weighted angle distance
    distance = wPerpendicular * pDistance + wLateral * latDistance + wAngle * angDistance

    # to test weighted distance
    print(distance)


def angle(line1, line2):
    # finding the vectors of line 1 and line 2
    vector1 = [line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]]
    vector2 = [line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]]

    # calculating the unit vectors, giving the directions of the vectors
    unitVector1 = vector1 / np.linalg.norm(vector1)
    unitVector2 = vector2 / np.linalg.norm(vector2)

    # performing the dot product
    dotProduct = np.dot(unitVector1, unitVector2)
    angle = np.arccos(dotProduct)
    return angle


def perpendiculardistance(line1, line2):
    # extracting the y coordinates of the two line segments
    line1YCoords = [line1[1][1], line1[0][1]]
    line2YCoords = [line2[1][1], line2[0][1]]

    # sorting the x coordinates to ascending order
    line1YCoords.sort()
    line2YCoords.sort()

    # first case: line 2 is within boundaries of line 1
    if line2YCoords[0] in range(line1YCoords[0], line1YCoords[1]) and line2YCoords[1] in range(line1YCoords[0], line1YCoords[1]):

        # calculate the perpendicular distance between line 1 and line 2
        yStartDiff = line2YCoords[0] - line1YCoords[0]
        yEndDiff = line2YCoords[1] - line1YCoords[1]
        perDist = (math.pow(yStartDiff, 2) + math.pow(yEndDiff, 2)) / (yStartDiff + yEndDiff)
        return perDist

    # second case: line 1 is within boundaries of line 2
    elif line1YCoords[0] in range(line2YCoords[0], line2YCoords[1]) and line1YCoords[1] in range(line2YCoords[0], line2YCoords[1]):
        
        # calculate the minimum distance between line 1 and line 2
        perDist = min(line1YCoords[0] - line2YCoords[0], line2YCoords[1] - line1YCoords[1])
        return perDist

    # third case: if both lines are not in boundaries of each other, return a default distance
    else:
        perDist = 10
        return perDist 

def lateraldistance(line1, line2):
    # extracting the x coordinates of the two line segments
    line1XCoords = [line1[1][0], line1[0][0]]
    line2XCoords = [line2[1][0], line2[0][0]]

    # sorting the x coordinates to ascending order
    line1XCoords.sort()
    line2XCoords.sort()

    # first case: line 2 is within boundaries of line 1
    if line2XCoords[0] in range(line1XCoords[0], line1XCoords[1]) and line2XCoords[1] in range(line1XCoords[0], line1XCoords[1]):

        # calculate the minimum distance between line 1 and line 2
        latDist = min(line2XCoords[0] - line1XCoords[0], line1XCoords[1] - line2XCoords[1])
        return latDist

    # second case: line 1 is within boundaries of line 2
    elif line1XCoords[0] in range(line2XCoords[0], line2XCoords[1]) and line1XCoords[1] in range(line2XCoords[0], line2XCoords[1]):
        
        # calculate the minimum distance between line 1 and line 2
        latDist = min(line1XCoords[0] - line2XCoords[0], line2XCoords[1] - line1XCoords[1])
        return latDist

    # third case: if both lines are not in boundaries of each other, return a default distance
    else:
        latDist = 10
        return latDist 