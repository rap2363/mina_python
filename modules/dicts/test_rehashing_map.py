import pytest
from .rehashing_map import RehashMapDictionary

def test_rehashing():
    d = RehashMapDictionary(2)
    d.add('fruit','apple')

    assert d.get('fruit') == 'apple'
    assert d.num_bins == 2

    d.add('transport','car')
    #this should trigger a rehash because load factor is now 1
    assert d.num_bins == 4

    assert d.get('fruit') == 'apple'
    assert d.get('transport') == 'car'