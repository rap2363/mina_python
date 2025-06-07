

class ImmutableList:
    def __init__(self, input_list):
        updated_list = []
        #copying input_list
        for i in input_list:
            updated_list.append(i)
        self.backing_list = updated_list

    def append(self, item):
        modified_list = []
        for i in self.backing_list:
            modified_list.append(i)
        modified_list.append(item)
        return ImmutableList(modified_list)

    def __getitem__(self, i):
        return self.backing_list[i]
    
    ##doesn't the concept of __setitem__ defeat the purpose of immutablity here?
    def __setitem__(self, i, value):
        raise TypeError("ImmutableList does not support")

