import pytest
from .list_dict import ListDict
from .sorted_list_dict import SortedListD

def test_add_and_get_single_item():
    d = SortedListD()
    d.add("a", 1)
    assert d.get("a") == 1 

def test_add_multiple_and_sort():
    d = SortedListD()
    d.add("c", 1)
    d.add("b", 2)
    d.add("a", 3)
    assert d.store == sorted(d.store)