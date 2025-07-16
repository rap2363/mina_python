'''
Thoughts:
valid path from start to finish
1. segment where total distance is less than C between recharge. Only move along path where distance within two nodes is less than C meters
2. stop at charging stations when needed
3. lowest possible distance from start to finish (regardless of no of stops/refilling)

** keep track of remaining distance at every point in time?
'''

import heapq

def dijkstra(graph, start, goal):
    # Set initial distances to infinity, except for start node
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
   
    predecessors = {} 
    for node in graph:
        predecessors[node] = None
    
    #using priority queue to track (distance,node)
    priority_queue = [(0, start)]  
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) #remove node with least distance from queue
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break
        
        #Update distances to neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            
            # If new distance is shorter, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances, predecessors

def shortest_path(predecessors, start, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    path.reverse()
    if path[0]== start:
        return path
    else:
        return [] 

