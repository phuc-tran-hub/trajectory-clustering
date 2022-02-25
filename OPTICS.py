# input: a set of line segments D = {L1, Lnum}
#        two parameters epsilon and minLines
# output: a set of clusters

from collections import deque
from TRACLUSdistance import traclusDistance

def opticsclustering(DL, eps, minLns):

    # starting clustering ID
    clusterID = 0

    for line in DL:
        if line.clusterID == "unclassified":

            adjLines = numberepsilon(line, DL, eps)

            if len(adjLines) >= minLns:
                for adjLine in adjLines:
                    adjLine.clusterID = clusterID

                # add all the adjacent neighbors into queue
                queue = deque()
                for adjLine in adjLines:
                    queue.append(adjLine) 

                expandcluster(queue, clusterID, DL, eps, minLns)
                clusterID += 1
                
            else:
                line.clusterID = "noise"

#     # Allocating the lines to their clusters
#     clusters = [[]]
#     for cluster in clusters:
#          if len(cluster) < minLns:
#              # remove cluster from the set of clusters
#             pass

    return DL
    
def numberepsilon(target, DL, eps):

    adjLines = [] 

    for line in DL:
        if line != target:
            if traclusDistance(target.lineSeg, line.lineSeg) < eps: 
                adjLines.append(line)
    
    return adjLines

def expandcluster(queue, clusterID, DL, eps, minLns):
    while len(queue) > 0:
        lineSegment = queue.pop()
        adjLines = numberepsilon(lineSegment, DL, eps)
        if len(adjLines) >= minLns:
            for adjLine in adjLines:
                if adjLine.clusterID == "unclassified" or adjLine.clusterID == "noise":
                    adjLine.clusterID = clusterID

                if adjLine.clusterID == "unclassified":
                    queue.append(adjLine)
