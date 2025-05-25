from .list_dict import ListDict  #since it's following the same structure

class SortedListD(ListDict):  #inheritance

    def add(self,key,value):
        super().add(key,value)  #using super so I don't have to duplicate the method
        self.store.sort() #adding a sort funtion to ensure list is alphabetically orderable
    
