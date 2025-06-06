from .dictionary import Dictionary

#using a hash function
class RehashMapDictionary(Dictionary):


    def __init__(self, num_bins):   
        self.num_bins = num_bins
        self.bin = []
        for i in range(self.num_bins):
            self.bin.append([]) 
        self.size = 0 #total number of elements

    def add(self,key,value):
        index = hash(key) %  self.num_bins     
        
        for i, (k,v) in enumerate(self.bin[index]):
            if k == key:
                self.bin[index][i] = (key,value)  #updates the existing key
                return
        else:
            default_load_factor = 0.5
            load_factor = self.size / self.num_bins

            if load_factor >= default_load_factor:
                self.rehash()
                index = hash(key) %  self.num_bins #recalculating index for new bins
                
            self.bin[index].append((key,value))
            self.size += 1

    def rehash(self):
        old_bin = self.bin
        self.num_bins *= 2
        self.bin = []
        for i in range(self.num_bins):
            self.bin.append([])
        self.size = 0

        #reinsert values into new bin
        for bin in old_bin:
            for key,value in bin:
                self.add(key,value)  

    def get(self,key):
        index = hash(key) %  self.num_bins 
        for k,v in self.bin[index]:
                if k == key:
                    return v
        return None
