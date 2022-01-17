# Name: Phuc Tran
# Date: January 5th, 2022
# Title: distance.c
# Description: calculate an abstract weighted distance function between two line segments

# Libraries
import numpy as np
import math

'''calculate the distance between two line segments.'''
def traclusDistance(line1, line2):
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
    # finding the vectors of line 1 and line 2
    # [1][0] = xEnd [0][0] = xStart
    # [1][1] = yEnd [0][1] = yStart

    vector1XSegment = line1[1][0] - line1[0][0]
    vector1YSegment = line1[1][1] - line1[0][1]

    vector2XSegment = line2[1][0] - line2[0][0]
    vector2YSegment = line2[1][1] - line2[0][1]

    vector1 = [vector1XSegment, vector1YSegment]
    vector2 = [vector2XSegment, vector2YSegment]

    # calculate the distance between two vectors
    dist1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
    dist2 = math.sqrt(vector2[0]**2 + vector2[1]**2)

    # IMPORTANT: Si and Ei is the longer vector, Sj and Ej is the shorter vector
    longerVector = 1 if dist1 > dist2 else 2
    
    projectionStart = 0
    projectionEnd = 0

    perpendiculardistance = 0

    # if vector 1 is the longer vector, project vector 2 onto vector 1
    if longerVector == 1:

        # calculating projectionStart
        SiSjVector = [line2[0][0] - line1[0][0], line2[0][1] - line1[0][1]]
        SiEiVector = vector2.copy()

        dotProduct1 = np.dot(SiSjVector, SiEiVector)
        magnitude1 = np.linalg.norm(SiEiVector)

        u1 = dotProduct1/magnitude1

        projectionStart = line1[0][0] + u1 * SiEiVector

        # calculating projectionEnd
        SiEjVector = [line2[1][0] - line1[0][0], line2[1][1] - line1[0][1]]
        dotProduct2 = np.dot(SiEjVector, SiEiVector)
        magnitude2 = np.linalg.norm(SiEiVector)

        u2 = dotProduct2/magnitude2

        projectionEnd = line1[0][0] + u2 * SiEiVector

        # calculate distance between SjPs and EjPe
        Lperpendicular1 = math.sqrt((line2[0][0] - projectionStart[0])**2 + (line2[1][0] - projectionEnd[0])**2)

        Lperpendicular2 = math.sqrt((line2[1][0] - projectionEnd[0])**2 + (line2[1][1] - projectionEnd[1])**2)

        # calculate perpendicular distance 
        perpendiculardistance = (Lperpendicular1 * Lperpendicular1 + Lperpendicular2 * Lperpendicular2) / (Lperpendicular1 + Lperpendicular2)

    # if vector 2 is the longer vector, project vector 1 onto vector 2
    elif longerVector == 2:

        # calculating projectionStart
        SiSjVector = [line1[0][0] - line2[0][0], line1[0][1] - line2[0][1]]
        SiEiVector = vector1.copy()

        dotProduct1 = np.dot(SiSjVector, SiEiVector)
        magnitude1 = np.linalg.norm(SiEiVector)

        u1 = dotProduct1/magnitude1

        projectionStart = line2[0][0] + u1 * SiEiVector

        # calculating projectionEnd
        SiEjVector = [line1[1][0] - line2[0][0], line1[1][1] - line2[0][1]]
        dotProduct2 = np.dot(SiEjVector, SiEiVector)
        magnitude2 = np.linalg.norm(SiEiVector)

        u2 = dotProduct2/magnitude2

        projectionEnd = line2[0][0] + u2 * SiEiVector

        # calculate distance between SjPs and EjPe
        Lperpendicular1 = math.sqrt((line1[0][0] - projectionStart[0])**2 + (line1[1][0] - projectionEnd[0])**2)

        Lperpendicular2 = math.sqrt((line1[1][0] - projectionEnd[0])**2 + (line1[1][1] - projectionEnd[1])**2)

        # calculate perpendicular distance 
        perpendiculardistance = (Lperpendicular1 * Lperpendicular1 + Lperpendicular2 * Lperpendicular2) / (Lperpendicular1 + Lperpendicular2)

    return perpendiculardistance

def lateraldistance(line1, line2):
    # finding the vectors of line 1 and line 2
    vector1 = [line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]]
    vector2 = [line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]]