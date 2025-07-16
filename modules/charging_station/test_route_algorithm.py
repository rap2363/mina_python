import pytest
from .route_algorithm import dijkstra, shortest_path


def test_shortest_path():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}        
    }
    distances, predecessors = dijkstra(graph, 'A','D')
    assert distances['D'] == 4
    path = shortest_path(predecessors, 'A', 'D')
    assert path == ['A','B','C','D']

def test_shortest_path():
    graph = {
        'A': {'B': 10, 'C': 4},
        'B': {'C': 3, 'D': 5},
        'C': {'D': 8},
        'D': {}        
    }    
    distances, predecessors = dijkstra(graph, 'A','D')
    assert distances['D'] == 12
    path = shortest_path(predecessors, 'A', 'D')
    assert path == ['A','C','D']