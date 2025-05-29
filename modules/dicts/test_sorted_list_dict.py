import pytest
from .sorted_list_dict import SortedListD

def test_add_and_get_single_item():
    d = SortedListD()
    d.add("a", 1)
    assert d.get("a") == 1 

def test_add_multiple_and_sort():
    d = SortedListD()
    d.add("cat", 1)
    d.add("boy", 2)
    d.add("able", 3)
    results = [["able", 3],["boy", 2],["cat", 1]]
    assert d.SortedL == results

def test_search_key():
    d = SortedListD()
    d.add("able", 1)
    d.add("boy", 2)
    d.add("cat", 3)
    assert d.get("cat") == 3