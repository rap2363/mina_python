Suppose we have a directed, weighted graph (G = (V, E)) with vertices (nodes). 
A node is connected to another node with an edge whose weight represents the shortest path distance from that node to the other. 
So for example, if nodes A and B represent two charging stations and the shortest path route from A->B is 1500 meters, 
then we’ll have an edge with weight 1500 that connects A->B. Note: Edges are not bidirectional!
For example, the edge that points from B->A may not have a weight of 1500 (because the route home is not literally the route to work driven backwards!).
Some of the nodes are special. Specifically, they represent charging stations. We can route through these to “fuel up” our vehicle.
Goal: Design an algorithm that solves the capacitated routing problem. We want to find the shortest path between two nodes in our graph, 
but we can only travel C meters before having to “refill” at a charging station. You can assume that charging is instantaneous.
