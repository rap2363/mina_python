from .dictionary import Dictionary

class ListDict(Dictionary):
    def __init__(self):
        self.store = []  # creating an empty list since dictonaries aren't allowed

    def add(self, key, value):
        for data in self.store:
            if data[0] == key:
                data[1] = value
                return
        self.store.append([key,value])

    def get(self, key):
        for data in self.store:
            if data[0] == key:
                return data[1]

        return None #after iterating through the list
