import heapq
from graph import *

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for nxt in graph.adj(current):
            new_cost = cost_so_far[current] + nxt[1]
            if nxt[0] not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(goal, nxt)
                frontier.put(nxt, priority)
                came_from[nxt] = current
    
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

def getNeighbors(i):
    
    out = [i-10, i+10]
    # when converting to python3 make sure this integer divides
    if (i-1)/10 == i/10:
        out += [i-11, i-1, i+9]
    if (i+1)/10 == i/10:
        out += [i-9, i+1, i+11]
    
    def f(x):
        return (x > 0 and x < 10201)
    
    return list(filter(f, out))

G = graph()
G.addVertex(10201)
for i in range(10201):
    N = getNeighbors(i)
    for n in N:
        G.addEdge(i, n, False, 1)




print a_star_search(G, start, goal)
