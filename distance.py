# Name: Phuc Tran
# Date: January 5th, 2022
# Title: distance.c
# Description: calculate an abstract weighted distance function between two line segments

# Libraries
import numpy as np

'''calculate the distance between two line segments.'''
def distance(line1, line2):
    # the distance threshold to determine similar line segments
    epsilon = 10

    # the weight of each lines
    wPerpendicular = 0
    wLateral = 0
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
    # TODO: find the perpendicular distance
    return 10


def lateraldistance(line1, line2):
    return 10