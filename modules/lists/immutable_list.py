

class ImmutableList:
    def __init__(self, input_list):
        self.backing_list = input_list[:]

    def __getitem__(self, i):
        return self.backing_list[i]
    
    def __setitem__(self, i, value):
        raise TypeError("ImmutableList does not support")

