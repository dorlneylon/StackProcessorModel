class IO:
    def __init__(self):
        self.buffers = [[0]*8]*8
    def __call__(self, command, data):
        if "in" in command:
            command = command.replace("in", "")
            return self.buffers[int(command)]
        if "out" in command:
            self.buffers[int(command.replace("out", ""))] = data
    def read(self, n, buffer_number=0):
        return self.buffers[buffer_number][0:n]
    def write(self, data):

