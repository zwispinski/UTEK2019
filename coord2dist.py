import numpy as np

def coord2dist(C):

    def distance(P, Q):
        return ( (P[0] - Q[0])**2 + (P[1] - Q[1])**2 )**0.5
    
    # C is a list of coordinates
    dist = np.zeros([len(C), len(C)])
    for i in range(len(C)):
        for j in range(len(C)):
            dist[i,j] = distance(C[i], C[j])
    return dist
