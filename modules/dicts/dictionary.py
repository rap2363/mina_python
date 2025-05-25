from typing import Protocol

class Dictionary(Protocol):
    def add(key, value):
        # This should add a new key value pair to the dictionary and *remove* any existing ones.
        ...

    def get(key):
        # This should return the value associated with this key if it exists, otherwise `None`
        ...
"""class MyDict:
    def __init__(self):
        self.storage = {}

    def add(self, key, value):
        self.storage[key] = value

    #if get(key) retrives the assigned value to the key
    def get(self, key):
        if key in self.storage:
            return self.storage[key]
        else :
            return None
            """