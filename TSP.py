from coord2dist import coord2dist
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

def TSP(dist_matrix, num_routes, depot):
    
    # Distance callback
    def create_distance_callback(dist_matrix):
        # Create a callback to calculate distances between cities.

        def distance_callback(from_node, to_node):
            return int(dist_matrix[from_node][to_node])

        return distance_callback

    tsp_size = len(dist_matrix[0])
    
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback.
        dist_callback = create_distance_callback(dist_matrix)
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            # Solution distance.
            print("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
            # Display the solution.
            routes = []
            for route_number in range(routing.vehicles()):
                node = routing.Start(route_number) # Index of the variable for the starting node.
                #route_str = ''
                route = []
                
                while not routing.IsEnd(node):
                    # Convert variable indices to node indices in the displayed route.
                    #route_str += str(routing.IndexToNode(index)) + ' -> '
                    index = routing.NodeToIndex(node)
                    route.append(index)
                    node = assignment.Value(routing.NextVar(node))
                #route_str += str(routing.IndexToNode(index))
                #print "Route:\n\n" + route_str
                routes.append(route)
        else:
            print('No solution found.')
            return []
    else:
        print('Specify an instance greater than 0.')
        return []
    return routes

from random import randint

R = []
for i in range(100):
    R += [ [randint(0,101), randint(0,101)] ]

#C = [ [0,0], [100, 0], [100, 1], [0, 100], [1, 100] ]
print(TSP(coord2dist(R), 1, 0))
