# input: a set of line segments D = {L1, Lnum}
#        two parameters epsilon and minLines
from collections import deque

def opticsclustering(DL, eps, minLns):
    clusterID = 0
    for line in DL:
        line.clusterID = "unclassified"


    for line in DL:
        if line.clusterID == "unclassified":

            adjLines = numberepsilon(line)
            print("compute")

            if adjLines >= minLns:
                for adjLine in adjLines:
                    adjLine.clusterID = clusterID

                # add all the adjacent neighbors into queue
                queue = deque()
                queue.append(adjLines)
                expandcluster(queue, clusterID, eps, minLns)
                clusterID += 1
            else:
                line.clusterID = "noise"

    # Allocating the lines to their clusters
    clusters = [[]]
    for cluster in clusters:
         if len(cluster) < minLns:
             # remove cluster from the set of clusters
            pass


def numberepsilon(line):
    return []

def expandcluster(queue, clusterID, eps, minLns):
    while len(queue) > 0:
        lineSegment = queue.pop()
        adjLines = numberepsilon(lineSegment)
        if adjLines >= minLns:
            for adjLine in adjLines:
                if adjLine.clusterID == "unclassified" or adjLine.clusterID == "noise":
                    adjLine.clusterID = clusterID

                if adjLine.clusterID == "unclassified":
                    queue.append(adjLine)
