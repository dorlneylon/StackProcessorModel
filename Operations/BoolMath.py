import json
import math
class BoolMath:
    def __init__(self):
        try:
            self.iops = json.load(open("opcode_set.json"))['logical_operations']
        except:
            self.iops = {}
        self.x = 0
        self.log = []
    def __call__(self, opcode, handler):
            
        if opcode not in self.iops:
            return None
        
        if opcode == "land":
            self.x = 0
            self.x = handler.pop()
            self.x = self.x & handler.pop()
            handler.push(self.x)
        if opcode == "lor":
            self.x = 0
            self.x = handler.pop()
            self.x = self.x | handler.pop()
            handler.push(self.x)
        if opcode == "lxor":
            self.x = 0
            self.x = handler.pop()
            self.x = self.x ^ handler.pop()
            handler.push(self.x)
        if opcode == "lnot":
            self.x = 0
            self.x = handler.pop()
            self.x = ~self.x
            handler.push(self.x)
        if opcode == "lrol":
            self.x = 0
            self.x = handler.pop()
            # реализовать потом
            handler.push(self.x)
        if opcode == "lror":
            self.x = 0
            self.x = handler.pop()
            # реализовать потом
            handler.push(self.x)
        if opcode == "lshl":
            self.x = 0
            self.x = handler.pop()
            # реализовать потом
            handler.push(self.x)
        if opcode == "lshr":
            self.x = 0
            self.x = handler.pop()
            # реализовать потом
            handler.push(self.x)
        return self.x
                                

