#all the import statements
from item import item
from readFile import readFile
from writeFile import writeFile
#from knapsack import knapsack
#from tsp import tsp
#from dijkstra import diskstra
#from distance import distance
from graph import graph # fix this line based on the 
import numpy

filename = "Competition\ Package/5a.in"


#read the file input and create a graph of items and robots

lines = readFile(filename)
#numbering things 
numberingList = lines[0].split(",")
numberOfRobots = int(numberingList[0].strip(),10)
numberOfItems = int(numberingList[1].strip(),10)
numberOfObstacles = int(numberingList[2].strip(),10)
#make the list of robots
robots = []
for i in range(numberOfRobots):
	robots += [[i,0]]
#make the list of items
items = []
for i in range(numberOfItems):
	itemInfo = lines[i+1]
	createdItem = item(itemInfo)
	items+= createdItem

#create list of obstacles
obstacles = []
for i in range (numberOfObstacles):
	a=lines[numberOfRobots+numberOfItems+i]
	a=a.lstrip('(')
	a=a.rstrip(')')
	b=a.split(', ')
	c=[]
	for num in b:
		c.append(int(num,10))
	obstacles.append(c)

#create graph given the obstacles
graphy = graph()
graphy.addVertex(10201)
for x in range(101):
	for y in range(101):
		if (x != 101 and y !=101):
			graphy.addVertex(coord2N([x,y]),coord2N([x+1,y+1]),FALSE,1)
		if (y != 0 and x !=101):
			graphy.addVertex(coord2N([x,y]),coord2N([x+1,y-1]),FALSE,1)
		if (x != 101):
			graphy.addVertex(coord2N([x,y]),coord2N([x+1,y]),FALSE,1)
		if (y != 101):
			graphy.addVertex(coord2N([x,y]),coord2N([x,y+1]),FALSE,1)
		

#partition the file input using the knapsack problem
for i in robots()
listOfObjectsInPartition = knapsack(list, location)

#implement the travelling salesman problem on each partition
#input to the tsp is distance matrix
#output of tps to be determined (string)
tps()

#perform each timestep while recording the robots' movements; involves robots yielding to other robots
#given this list use dijkstra on the big graph

dijkstraOutput = dijkstra(startLocation, endLocation)

#convert the output of dijkstra to a list of instructions for robot the robot



#functions to convert coordinates to n and vice versa
def coord2N(a):
    return 101* a[1] +a[0]

def N2coord(N):
    y=N//101
    x=N%101
    return [x,y]


