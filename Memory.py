class Memory:
    def __init__(self, memory_size):
        self.memory = [0 for _ in range(memory_size)]
        self.memory_size = memory_size
    def __call__(self, address, value):
        if address < 0 or address >= self.memory_size:
            raise Exception("Address out of range")
        self.memory[address] = value
    def read(self, address):
        if address < 0 or address >= self.memory_size:
            raise Exception("Address out of range")
        return self.memory[address]
    def write(self, address, value):
        if address < 0 or address >= self.memory_size:
            raise Exception("dAdress out of range")
        self.memory[address] = value

def test_memory():
    memory = Memory(10)
    memory(0, 10)
    assert memory.read(0) == 10
    memory.write(1, 20)
    assert memory.read(1) == 20
