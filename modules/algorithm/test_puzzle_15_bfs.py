import pytest
from puzzle_15_bfs import State

def test_breadth_first_search():
    x = [1,2,3,0,4,5,7,8,6]
    goal_state = [1,2,3,4,5,6,7,8,0]

    initial_state = State(x)
    path = initial_state.breadth_first_search(goal_state)

    expected_path = [
        (1, 2, 3, 0, 4, 5, 7, 8, 6),
        (1, 2, 3, 4, 0, 5, 7, 8, 6),
        (1, 2, 3, 4, 5, 0, 7, 8, 6),
        (1, 2, 3, 4, 5, 6, 7, 8, 0)
    ]

    assert path == expected_path

    y = [1,2,3,0,4,5,7,8,6]
    goal_state = [1,2,3,4,5,6,7,9,0]

    initial_state = State(y)
    result = initial_state.breadth_first_search(goal_state)

    assert result == tuple(y)