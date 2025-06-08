import pytest
from .immutable_list import ImmutableList


def test_set_item():
    x = ImmutableList([1, "hello", 3])
    y = x

    assert x[1] == "hello"

    with pytest.raises(TypeError):
        y[0] = 5