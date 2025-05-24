import pytest
from .list_dict import ListDict

def test_add_and_get_single_item():
    d = ListDict()
    d.add("a", 1)
    assert d.get("a") == 1

def test_overwrite_existing_key():
    d = ListDict()
    d.add("a", 1)
    d.add("a", 2)
    assert d.get("a") == 2

def test_get_nonexistent_key():
    d = ListDict()
    assert d.get("not_there") is None

def test_add_multiple_items():
    d = ListDict()
    d.add("a", 1)
    d.add("b", 2)
    d.add("c", 3)
    assert d.get("a") == 1
    assert d.get("b") == 2
    assert d.get("c") == 3

def test_order_independent_access():
    d = ListDict()
    keys = ["x", "y", "z"]
    values = [10, 20, 30]
    for k, v in zip(keys, values):
        d.add(k, v)
    for k, v in zip(keys, values):
        assert d.get(k) == v
