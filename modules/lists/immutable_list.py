

class ImmutableList:
    def __init__(self, input_list):
        self.backing_list = input_list[:]

#Here append creates a copy of the list, modifies it and makes it immutable
    def append(self, item):
        modified_list = self.backing_list[:]
        modified_list.append(item)
        return ImmutableList(modified_list)

    def __getitem__(self, i):
        return self.backing_list[i]
    
    def __setitem__(self, i, value):
        raise TypeError("ImmutableList does not support")

