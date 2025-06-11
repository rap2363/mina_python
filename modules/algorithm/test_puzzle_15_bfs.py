import pytest
from puzzle_15_bfs import State

def test_breadth_first_search():
    x = [1,2,3,0,4,5,7,8,6]
    goal_state = [1,2,3,4,5,6,7,8,0]

    initial_state = State(x)
    result = initial_state.breadth_first_search(x,goal_state)

    assert result == goal_state

    y = [1,2,3,0,4,5,7,8,6]
    goal_state = [1,2,3,4,5,6,7,9,0]

    initial_state = State(y)
    result = initial_state.breadth_first_search(y,goal_state)

    assert result == y