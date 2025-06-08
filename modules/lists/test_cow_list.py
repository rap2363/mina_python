import pytest
from .cow_list import CowList

def test_updating_value():
    x = CowList([1, 2, 3])
    y = x
    x = x.set_value(0, "hello")
    print(x) # This should print ["hello", 2, 3]
    print(y) # This should print [1, 2, 3]
    assert x.backing_list == ["hello", 2, 3]
    assert y.backing_list == [1, 2, 3]

    with pytest.raises(TypeError):
        x[0] = 5