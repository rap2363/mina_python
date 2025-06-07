

class CowList:
    def __init__(self, input_list):
        self.backing_list = input_list
        
    def __getitem__(self, i):
        return self.backing_list[i]   

    def append(self, item):
        modified_list = []
        for i in self.backing_list:
            modified_list.append(i)
        modified_list.append(item)
        return CowList(modified_list)

    def set_value(self, i, value):
        updated_list = []
        for k in self.backing_list:
            updated_list.append(k)       
        updated_list[i] = value
        return CowList(updated_list)