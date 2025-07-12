'''
Thoughts:
valid path from start to finish
1. segment where total distance is less than C between recharge. Only move along path where distance within two nodes is less than C meters
2. stop at charging stations when needed
3. lowest possible distance from start to finish (regardless of no of stops/refilling)

** keep track of remaining distance at every point in time?
'''

import heapq

def dijkstra(graph, start):
    # Set initial distances to infinity, except for start node
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
   
    predecessors = {} #tracking path
    for node in graph:
        predecessors[node] = None
    
    #using priority queue to track (distance,node)
    priority_queue = [(0, start)]  
    

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) #remove node with least distance from queue

        #if currrent distance is greater than stored distance skip
        if current_distance > distances[current_node]:
            continue
        
        #Update distances to neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            
            # If new distance is shorter, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances, predecessors

def reconstruct_path(predecessors, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    path.reverse()
    if path[0]== start:
        return path
    else:
        return [] 

#finding shortest distance between charging stations
def shortest_dist_between_stations(graph, stations):
    station_distances = {}
    for s in stations:
        station_distances[s] = {}
    
    station_predecessors = {}
    for s in stations:
        station_predecessors[s] = {}

    for source_station in stations:
        dist, pred = dijkstra(graph,source_station)
        for target_station in stations:
            if target_station != source_station:
                station_distances[source_station][target_station] = dist.get(target_station, float('inf'))
                station_predecessors[source_station][target_station] = pred
    
    return station_distances,station_predecessors

#build a reduced graph with nodes if distance <= capacity
def build_reduced_graph(station_distances,capacity):
    reduced_graph = {}
    for s in station_distances:
        reduced_graph[s] = {}

    for s, neighbors in station_distances.items():
        for t, dist in neighbors.items():
            if dist <= capacity:
                reduced_graph[s][t] = dist

    return reduced_graph

