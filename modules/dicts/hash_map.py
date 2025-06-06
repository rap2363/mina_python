"""
def get_bin_index(key):
    return (ord(k[0].lower()) - ord('a')) % N
"""
from .dictionary import Dictionary


#using a hash function
class HashMapDictionary(Dictionary):
    def __init__(self, num_bins):   
        self.num_bins = num_bins
        self.bin = []
        for i in range(self.num_bins):
            self.bin.append([]) 


    #def get_bin_index(self,key):
    #    return (ord(key[0].lower()) - ord('a')) % self.num_bins       

    def add(self,key,value):
        index = hash(key) %  self.num_bins     #using this to ensure it's still within range     
        # since each bin could hold multiple key pair values
        
        for i, (k,v) in enumerate(self.bin[index]):
            if k == key:
                self.bin[index][i] = (key,value)  #updates the existing key
                return
        else:
            self.bin[index].append((key,value))  #add new pair if no key found
            

        

    def get(self,key):
        index = hash(key) %  self.num_bins 
        for k,v in self.bin[index]:
                if k == key:
                    return v
        return None

