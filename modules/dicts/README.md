# Dictionaries

You should be familiar with the idea of dictionaries in Python, effectively a "key-value" structure used for quick retrieval based on a unique key, e.g.:
```
some_info = {
    'name': 'Ama',
    'age': 20,
    'interests': ['Coding', 'Afro beat', 'general hijinks']
}
```
and we are able to retrieve information via a call like `some_info['age']` (which should return 20). In this module we'll explore how we can implement
a dictionary *ourselves*. The goal of this is to learn about the following concepts:
1. `Interface` vs. `Implementation`: These concepts get confused often in coding and knowing the difference will help
   you be a much more powerful developer. For example, dictionaries are often referred to as "hash maps" in Python, but why is that? Is this right?
2. Fundamental algorithms: We'll explore some core skills (e.g. storage vs. time complexity, binary search, hashing and hash functions, etc.).

Each of the assignments here will be a different way of implementing a dictionary in Python. We'll do so by implementing the following API:

```
class Dictionary(Protocol):
    def add(key, value):
        # This should add a new key value pair to the dictionary and *remove* any existing ones.
        ...

    def get(key):
        # This should return the value associated with this key if it exists, otherwise `None`
        ...
```

This is the `interface` we'll implement.

## Assignment 1: Dict as a List

The first assignment is to implement this dictionary in a *very* simple way. Specifically, we'll implement it as a list of key-value pairs.
Write this implementation in `list_dict.py`.

1. What is the time complexity of adding new key-values? What about retrieving them?
2. What's the storage complexity?

## Assignment 2: Dict as a Sorted List

For assignment 1 the implementation is simple, but it's particularly inefficient. What if we had some nice guarantees on the keys? For example,
what if we could *sort* them? Could we improve the time complexity of this algorithm? Write your implementation in `sorted_list_dict.py`

1. What is the time complexity of adding new key-values? What about retrieving them?
2. What's the storage complexity? Is it worse than before? Or the same?
3. What does this new *sortable* constraint mean for the *kinds* of keys we can put in our dictionary? 

## Assignment 3: Implement a Set!

You know what sets are in Python right? You can do things like: `x = set([1, 2, 3])` and then `if y in x: print(y)` or something. Here's a concrete
for the Set class:

```
class Set:
    def __init__(self, dict: Dictionary):
        self._dict = dict

    def add(value):
        # Add a value to the set
        ...

    def contains(value):
        # Check whether the value exists
        ...
    
    def remove(value):
        # Remove the value
        ...
```

And look! It takes in a `dict` as part of its constructor. Specifically, one of *your* implementations of Dictionary! So we're going to implement these
methods on Set by *using* your Dictionary interface! Note that the `Set` class doesn't need to know *which* implementation of Dictionary will actually
get passed in! Add your implementation to set.py!

## Assignment 4: Dict as a Hash Map

Now we're going to really get cooking. So far we've been able to leverage the "sortability" of our keys to make accesses/insertions into the dictionary relatively fast. But there's actually an even faster way to do this in principle.

Imagine we have a list of "bins" for our data to go in. Each bin is indexed, 0, 1, 2, 3... up to N-1 for N bins. Now when we want to add a key-value into our dictionary, we'll have to put the key-value in one of our bins. In other words, we need a way to *deterministically* map from a key to a bin index. One way we could do this is to just take the first character of our key (if it's a string), map it to a number (e.g. A-->0, B-->1, C-->2, ..., Z-->25), and then take the *modulus* of that number with the number of bins we have.

In Python, this looks like 
```
def get_bin_index(key):
    return (ord(k[0].lower()) - ord('a')) % N
```
### What if two values map to the same bin?
So for example, if we have two string that start with the same character (or happen to mod to the same bin), we would have a *collision*. There are multiple ways to solve this, but for right now we'll just say we can have a *list* of key-values per bin. So in other words, our bins themselves will be lists that can hold multiple key-values.


Implement this in hash_map.py:

```
class HashMapDictionary(Dictionary):
    def __init__(self, num_bins):
        self.num_bins = num_bins

    def add(value):
        # Add a value to the set
        ...

    def contains(value):
        # Check whether the value exists
        ...
    
    def remove(value):
        # Remove the value
        ...
```
Questions to think through as we get going:
1. How many bins should we have? How would we know this in advance?
2. Clearly this would be really bad if we stored a bunch of strings that happened to start with the same character. What are ways we could make this faster by changing how we calculate the bin index for some data?
3. What happens as we continue adding more and more data to this data structure? What will happen to our lookup times?
