from typing import Protocol

class Dictionary(Protocol):
    def add(key, value):
        # This should add a new key value pair to the dictionary and *remove* any existing ones.
        ...

    def get(key):
        # This should return the value associated with this key if it exists, otherwise `None`
        ...
