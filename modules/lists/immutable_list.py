import copy

class ImmutableList:
    def __init__(self, input_list):
        self.backing_list = input_list
        self.updated_list = copy.deepcopy(self.backing_list)

    def append(self, item):
        modified_list = copy.deepcopy(self.updated_list)
        modified_list.append(item)
        return ImmutableList(modified_list)

    def __getitem__(self, i):
        return self.updated_list[i]
    
    ##doesn't the concept of __setitem__ defeat the purpose of immutablity here?
    def __setitem__(self, i, value):
        raise TypeError("ImmutableList does not support")

