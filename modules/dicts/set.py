from .sorted_list_dict import SortedListD
from .list_dict import ListDict

class Set:
    def __init__(self, dict: SortedListD):
        self._dict = dict

    def add(self,value):
        # Add a value to the set
        self._dict.add(value,True) 

    def contains(self,value):
        # Check whether the value exists
        if self._dict.get(value) is not None:
            return True
        else :
            return False
    
    def remove(self,value):
        # Remove the value
        if self.contains(value) == True :
            self._dict.remove(value)
        


