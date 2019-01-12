import numpy as np
from distance import distance

def coord2dist(C):

    # C is a list of coordinates
    dist = np.zeros([len(C), len(C)])
    for i in range(len(C)):
        for j in range(len(C)):
            dist[i,j] = distance(C[i], C[j])
    return dist
