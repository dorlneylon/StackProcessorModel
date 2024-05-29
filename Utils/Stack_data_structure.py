class Stack_data_structure:
    def __init__(self, max_size = 10):
        self.array = []*max_size
        self.top = 0
    def push(self, item):
        if self.top == len(self.array):
            return None
        else:
            self.array[self.top] = item
            self.top += 1
    def pop(self):
        if self.top == 0:
            return None
        else:
            self.top -= 1
            return self.array[self.top]
    def top(self):
        if self.top == 0:
            return None
        else:
            return self.array[self.top-1]
                


                