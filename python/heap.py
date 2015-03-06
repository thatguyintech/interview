class Heap:
    def __init__(self, values=[]):
        self.data = [None]*32
        if len(values) > 1:
            self.insert_values(values)
        elif len(values) == 1:
            self.insert(values)
    def insert(self, value):
        try:
            current_index = len(self.data)
            self.data[current_index] = value
            correct_order = false
            while not correct_order:
                parent_index = (current_index - 1)/2
                if self.data[parent_index] < self.data[current_index]:
                    temp = self.data[parent_index]
                    self.data[parent_index] = self.data[current_index]
                    self.data[current_index] = temp
                else:
                    correct_order = true
        except IndexError:
            new_data = self.data*2
            for i in range(len(self.data), len(self.data)*2):
                new_data[i] = None
            self.data = new_data
            self.insert(value)
            
        return
    def insert_values(self, values):
        return


