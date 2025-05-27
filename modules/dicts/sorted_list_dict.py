
from .dictionary import Dictionary  

class SortedListD(Dictionary):
    def __init__(self):
        self.SortedL = [] #creating an empty list

    def add(self,key,value):
        left = 0
        right = len(self.SortedL) -1
        while left <= right:
            middle = (left+right)//2
            
            if self.SortedL[middle][0] == key:
                self.SortedL[middle][1] = value
                return
            elif self.SortedL[middle][0] < key:
                left = middle + 1
            else:
                right = middle -1
        #if key not in list
        self.SortedL.insert(left,[key,value])

    #using a custom function
    def get(self,key):
        left = 0
        right = len(self.SortedL) - 1
        while left <= right:
            middle = (left+right)// 2
        
            if self.SortedL[middle][0] == key:
                return self.SortedL[middle][1]
            elif self.SortedL[middle][0] > key:
                right = middle - 1
            elif self.SortedL[middle][0] < key:
                left = middle + 1
        return None