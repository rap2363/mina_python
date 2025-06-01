
"""
def get_bin_index(key):
    return (ord(k[0].lower()) - ord('a')) % N
"""
from .dictionary import Dictionary



class HashMapDictionary(Dictionary):
    def __init__(self, num_bins):   
        self.num_bins = num_bins
        self.set_index()

    def set_index(self): #creating a bin for mutiple paired item
        self.bin = []
        for index in range(self.num_bins):
            self.bin.append([index, []])

    def get_bin_index(self,key):
        return (ord(key[0].lower()) - ord('a')) % self.num_bins       

    def add(self,key,value):
        index = self.get_bin_index(key)             
        for data in self.bin:
            if data[0] == index:
                # since each bin could hold multiple key pair values
                for i, (k,v) in enumerate(data[1]):
                    if k == key:
                        data[1][i] = (key,value)
                        return
                else:
                    data[1].append((key,value))
                return
            

        ...

    def get(self,key):
        index = self.get_bin_index(key)

        for data in self.bin:
            if data[0] == index:
                for k,v in data[1]:
                    if k == key:
                        return v
        return None


    
    def remove(self,key):
        index = self.get_bin_index(key)

        for data in self.bin:
            if data[0] == index:
                for i, (k,v) in enumerate(data[1]):
                    if k == key:
                        del data[1][i]
                        return

