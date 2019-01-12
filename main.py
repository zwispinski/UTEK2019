#all the import statements
from item import item
from readFile import readFile
from writeFile import writeFile
#from knapsack import knapsack
#from tsp import tsp
#from dijkstra import diskstra
#from distance import distance
import numpy

filename = "Competition Package/5a.in"


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
obstacles = 

#create graph with given the obstacles


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





