import pytest
from .list_dict import ListDict
from .sorted_list_dict import SortedListD
from .set import Set

def test_add_and_contains():
    s = Set(SortedListD())
    s.add("a")
    assert s.contains("a") == True
    assert s.contains("c") == False #since the value "c" wasn't add to the list

def test_add_and_remove():
    s = Set(SortedListD())
    s.add("c")
    assert s.contains("c") == True
    s.remove("c")
    assert s.contains("c") == False
    
    s.remove("b") #checking for a non existing value
    assert s.contains("b") == False
