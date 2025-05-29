
from .dictionary import Dictionary
class Set:
    def __init__(self, dict: Dictionary):
        self._dict = dict

    def add(self,value):
        # Add a value to the set
        self._dict.add(value,True) 

    def contains(self,value):
        # Check whether the value is True
        return self._dict.get(value) == True

    
    def remove(self,value):
        # Remove the value by setting to false
        if self.contains(value):
            self._dict.add(value,False)
        


