# Name: Phuc Tran
# Date: January 5th, 2022
# Title: distance.c
# Description: calculate an abstract weighted distance function between two line segments

# Libraries
from matplotlib import projections
import numpy as np
import math

def calculateLongerVector(line1, line2):
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
    
    # # testing which lengeth is correct
    # print("dist1", dist1)
    # print("dist2", dist2)
    
    return 1 if dist1 > dist2 else 2

def calculateProjection(line1, line2, longerVector):

    # calculating line segments
    vector1XSegment = line1[1][0] - line1[0][0]
    vector1YSegment = line1[1][1] - line1[0][1]

    vector2XSegment = line2[1][0] - line2[0][0]
    vector2YSegment = line2[1][1] - line2[0][1]

    vector1 = [vector1XSegment, vector1YSegment]
    vector2 = [vector2XSegment, vector2YSegment]

    # if vector 1 is the longer vector, project vector 2 onto vector 1
    if longerVector == 1:

       # calculating projectionStart
        SiSjVector = [line1[0][0] - line2[0][0], line1[0][1] - line2[0][1]]

        # print("SiSj Vector", SiSjVector)

        vector1XSegment = line1[0][0] - line1[1][0]
        vector1YSegment = line1[0][1] - line1[1][1]

        vector1 = [vector1XSegment, vector1YSegment]

        # print("SiEi Vector", vector2)

        # Calculating SiEi Vector
        SiEiVector = np.copy(vector1)
        dotProduct1 = np.dot(SiSjVector, SiEiVector)

        # print("dotProduct", dotProduct1)

        magnitude1 = np.linalg.norm(SiEiVector)
                
        u1 = dotProduct1/ (magnitude1 * magnitude1)

        # print("u1", u1)

        # print("product", u1 * SiEiVector)

        Si =[line1[0][0], line1[0][1]]

        projectionStart = Si - (u1 * SiEiVector)

        # print("projectionStart", projectionStart)

        # calculating projectionEnd
        SiEjVector = [line1[0][0] - line2[1][0], line1[0][1] - line2[1][1]]

        # print("SiEjVector", SiEjVector)

        dotProduct2 = np.dot(SiEjVector, SiEiVector)
        magnitude2 = np.linalg.norm(SiEiVector)

        u2 = dotProduct2/ (magnitude2 * magnitude2)

        projectionEnd = Si - (u2 * SiEiVector)

    # if vector 2 is the longer vector, project vector 1 onto vector 2
    elif longerVector == 2:

        # calculating projectionStart
        SiSjVector = [line2[0][0] - line1[0][0], line2[0][1] - line1[0][1]]

        # print("SiSj Vector", SiSjVector)

        vector2XSegment = line2[0][0] - line2[1][0]
        vector2YSegment = line2[0][1] - line2[1][1]

        vector2 = [vector2XSegment, vector2YSegment]

        # print("SiEi Vector", vector2)

        # Calculating SiEi Vector
        SiEiVector = np.copy(vector2)
        dotProduct1 = np.dot(SiSjVector, SiEiVector)

        # print("dotProduct", dotProduct1)

        magnitude1 = np.linalg.norm(SiEiVector)
                
        u1 = dotProduct1/ (magnitude1 * magnitude1)

        # print("u1", u1)

        # print("product", u1 * SiEiVector)

        Si =[line2[0][0], line2[0][1]]

        projectionStart = Si - (u1 * SiEiVector)

        # print("projectionStart", projectionStart)

        # calculating projectionEnd
        SiEjVector = [line2[0][0] - line1[1][0], line2[0][1] - line1[1][1]]

        # print("SiEjVector", SiEjVector)

        dotProduct2 = np.dot(SiEjVector, SiEiVector)
        magnitude2 = np.linalg.norm(SiEiVector)

        u2 = dotProduct2/ (magnitude2 * magnitude2)

        projectionEnd = Si - (u2 * SiEiVector)

    # print("projectionStart", projectionStart)
    # print("projectionEnd", projectionEnd)

    return projectionStart, projectionEnd

'''calculate the distance between two line segments.'''
def traclusDistance(line1, line2):
    # the weight of each lines
    wPerpendicular = .2
    wLateral = .5
    wAngle = .5
    
    pDistance = perpendiculardistance(line1, line2)
    # print("pDistance,", pDistance)
    latDistance = lateraldistance(line1, line2)
    # print("latDistance,", latDistance)
    angDistance = angle(line1, line2)
    # print("angDistance,", angDistance)

    # distance equals the weighted parallel distance plus weighted lateral distance plus weighted angle distance
    distance = wPerpendicular * pDistance + wLateral * latDistance + wAngle * angDistance

    # return distance
    return distance


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

    # IMPORTANT: Si and Ei is the longer vector, Sj and Ej is the shorter vector
    longerVector = calculateLongerVector(line1, line2)

    # calculating projectionStart and projectionEnd
    projectionStart, projectionEnd = calculateProjection(line1, line2, longerVector)

    perpendiculardistance = 0

    # if vector 1 is the longer vector, project vector 2 onto vector 1
    if longerVector == 1:

        # calculate distance between SjPs and EjPe (perpendicular Euclidean distance)
        Lperpendicular1 = math.sqrt( (line2[0][0] - projectionStart[0])**2 + (line2[0][1] - projectionStart[1])**2 )
        # print("Lperpendicular1", Lperpendicular1)

        Lperpendicular2 = math.sqrt( (line2[1][0] - projectionEnd[0])**2 + (line2[1][1] - projectionEnd[1])**2 )
        # print("Lperpendicular2", Lperpendicular2)

    # if vector 2 is the longer vector, project vector 1 onto vector 2
    elif longerVector == 2:

        # calculate distance between SjPs and EjPe (perpendicular Euclidean distance)
        Lperpendicular1 = math.sqrt( (line1[0][0] - projectionStart[0])**2 + (line1[0][1] - projectionStart[1])**2 )
        # print("Lperpendicular1", Lperpendicular1)

        Lperpendicular2 = math.sqrt( (line1[1][0] - projectionEnd[0])**2 + (line1[1][1] - projectionEnd[1])**2 )
        # print("Lperpendicular2", Lperpendicular2)

        
    # calculate perpendicular distance 
    perpendiculardistance = (Lperpendicular1 * Lperpendicular1 + Lperpendicular2 * Lperpendicular2) / (Lperpendicular1 + Lperpendicular2)

    return perpendiculardistance

def lateraldistance(line1, line2):
    # finding the vectors of line 1 and line 2
    vector1 = [line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]]
    vector2 = [line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]]

    longerVector = calculateLongerVector(line1, line2)

    # calculating projectionStart and projectionEnd
    projectionStart, projectionEnd = calculateProjection(line1, line2, longerVector)

    parallelDistance = 0

    # if vector 1 is the longer vector, project vector 2 onto vector 1
    if longerVector == 1:
        
        # calculate distance between SiPs (start of longer vector and the first projection point)
        Lparallel1 = math.sqrt((line1[0][0] - projectionStart[0])**2 + (line1[0][1] - projectionStart[1])**2)

        Lparallel2 = math.sqrt((line1[1][0] - projectionEnd[0])**2 + (line1[1][1] - projectionEnd[1])**2)   

        parallelDistance = min(Lparallel1, Lparallel2)

    # if vector 1 is the longer vector, project vector 2 onto vector 1
    elif longerVector == 2:

        # calculate distance between SiPs (start of longer vector and the first projection point)
        Lparallel1 = math.sqrt((line2[0][0] - projectionStart[0])**2 + (line2[0][1] - projectionStart[1])**2)

        Lparallel2 = math.sqrt((line2[1][0] - projectionEnd[0])**2 + (line2[1][1] - projectionEnd[1])**2)  

        parallelDistance = min(Lparallel1, Lparallel2)

    return parallelDistance