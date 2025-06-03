import pytest
from .hash_map import HashMapDictionary

def test_add_multiple_items():
    d = HashMapDictionary(3)
    d.add('fruit','apple')
    d.add('transport','car')
    d.add('hobby', 'hiking')
    
    assert d.get('transport') == 'car'
    assert d.get('fav') == None
    d.add('fav', 'food') 
    assert d.get('fav') == 'food'

def test_collision():
    d = HashMapDictionary(2)
    d.add('fruit', 'apple')
    d.add('family', 'nuclear')
    #testing data is not overriden
    assert d.get('fruit') == 'apple'
    assert d.get('family') == 'nuclear'

def test_remove_item():
    d = HashMapDictionary(4)
    d.add('fruit','apple')
    d.add('transport','car')
    d.add('hobby', 'hiking')

    d.remove('hobby')
    d.remove('family')
    assert d.get('hobby') == None
    assert d.get('family') == None