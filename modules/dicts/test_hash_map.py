import pytest
from .hash_map import HashMapDictionary

def test_add_multiple_items():
    d = HashMapDictionary(3)
    d.add('fruit','apple')
    d.add('transport','car')
    d.add('hobby', 'hiking')
    
    assert d.get('transport') == 'car'
    assert d.get('fav') == None

def test_remove_item():
    d = HashMapDictionary(4)
    d.add('fruit','apple')
    d.add('transport','car')
    d.add('hobby', 'hiking')

    d.remove('hobby')
    assert d.get('hobby') == None