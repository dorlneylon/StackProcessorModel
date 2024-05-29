from Memory import Memory
from DataType import DataType
class MemoryHandler:
    def __init__(self, ram: Memory):
        self.ram = ram
    def read(self, address: int):
        x = self.ram.read(address)
        if isinstance(x, DataType):
            return x.pure()
        else:
            return x
    def write(self, address: int, value: DataType):
        self.ram.write(address, value)
    
        

