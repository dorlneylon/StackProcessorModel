import json
class IntMath:
    def __init__(self):
        try:
            self.iops = json.load(open("../opcode_set.json"))['integer_operations']
        except:
            self.iops = {}
        self.x = 0
        self.log = []
    def __call__(self, opcode, handler):
        # "iadd", "isub", "imul", "idiv", "imod", "iabs", "iinc", "idec", "ineg", "itof"
        if opcode not in self.iops:
            return None
        if opcode == "iadd":
            self.x = 0 
            self.x += handler.pop()
            self.x += handler.pop()
            handler.push(self.x)
        if opcode == "isub":
            self.x = 0 
            self.x += handler.pop()
            self.x -= handler.pop()
            handler.push(self.x)
        if opcode == "imul":
            self.x = 0 
            self.x += handler.pop()
            self.x *= handler.pop()
            handler.push(self.x)
        if opcode == "idiv":
            self.x = 0 
            self.x += handler.pop()
            self.x = self.x // handler.pop()
            handler.push(self.x)
        if opcode == "imod":
            self.x = 0 
            self.x += handler.pop()
            self.x = self.x % handler.pop()
            handler.push(self.x)
        if opcode == "iabs":
            self.x = 0 
            self.x += handler.pop()
            self.x = abs(self.x)
            handler.push(self.x)
        if opcode == "iinc":
            self.x = 0 
            self.x += handler.pop()+1
            handler.push(self.x)
        if opcode == "idec":
            self.x = 0 
            self.x += handler.pop()-1
            handler.push(self.x)
        if opcode == "ineg":
            self.x = 0 
            self.x -= handler.pop()
            handler.push(self.x)
        return self.x
                                

