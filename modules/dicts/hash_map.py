"""
def get_bin_index(key):
    return (ord(k[0].lower()) - ord('a')) % N
"""
from .dictionary import Dictionary



class HashMapDictionary(Dictionary):
    def __init__(self, num_bins):   
        self.num_bins = num_bins
        self.bin = []
        for index in range(self.num_bins):
            self.bin.append([index, []]) 


    def get_bin_index(self,key):
        return (ord(key[0].lower()) - ord('a')) % self.num_bins       

    def add(self,key,value):
        index = self.get_bin_index(key)             
        # since each bin could hold multiple key pair values
        
        for i, (k,v) in enumerate(self.bin[index][1]):
            if k == key:
                self.bin[index][1][i] = (key,value)
                return
        else:
            self.bin[index][1].append((key,value))
            

        ...

    def get(self,key):
        index = self.get_bin_index(key)
        for k,v in self.bin[index][1]:
                if k == key:
                    return v
        return None

