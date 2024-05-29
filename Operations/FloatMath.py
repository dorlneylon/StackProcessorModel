import json
import math
class IntMath:
    def __init__(self, iops=None):

        if iops is None:
            try:
                self.iops = json.load(open("opcode_set.json"))['float_operations']
            except:
                self.iops = {}
        self.x = 0
        self.log = []
    def __call__(self, opcode, handler):
        # "fadd", "fsub", "fmul", "fdiv", "fabs", "fsqrt", "ftan", "fatan", "fpow2", "ftoi"
        if opcode not in self.iops:
            return None
        if opcode == "fadd":
            self.x = 0 
            self.x += handler.pop()
            self.x += handler.pop()
            handler.push(self.x)
        if opcode == "fsub":
            self.x = 0 
            self.x += handler.pop()
            self.x -= handler.pop()
            handler.push(self.x)
        if opcode == "fmul":
            self.x = 0 
            self.x += handler.pop()
            self.x *= handler.pop()
            handler.push(self.x)
        if opcode == "fdiv":
            self.x = 0 
            self.x += handler.pop()
            self.x = self.x / handler.pop()
            handler.push(self.x)
        if opcode == "fabs":
            self.x = 0 
            self.x += handler.pop()
            self.x = abs(self.x)
            handler.push(self.x)
        if opcode == "fsqrt":
            self.x = 0 
            self.x += handler.pop()
            self.x = math.sqrt(self.x)
            handler.push(self.x)
        if opcode == "ftan":
            self.x = 0 
            self.x += handler.pop()
            self.x = math.tan(self.x)
            handler.push(self.x)
        if opcode == "fatan":
            self.x = 0 
            self.x += handler.pop()
            self.x = math.atan(self.x)
            handler.push(self.x)
        if opcode == "fpow2":
            self.x = 0 
            self.x += handler.pop()
            self.x = math.pow(2, self.x)
            handler.push(self.x)
        return self.x
                                

