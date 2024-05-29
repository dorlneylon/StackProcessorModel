
import Memory
import Stack
import APU
import Registers
import CommandParser

class CU:
    def __init__(self):
        self.memory = Memory.Memory(1024*1024)
        self.stack = Stack.Stack(100)
        self.APU = APU.APU()
        self.registers = Registers.Registers()
        self.commandParser = CommandParser.CommandParser()
    def __call__(self):
        self.registers.IP += 1
        self.registers.AR = self.registers.IP
        data = self.memory.read(self.registers.AR)
        command, data = self.commandParser(data)
        self.APU(command, data)
    def loop(self):
        self.registers.IP += 1
        self.registers.AR = self.registers.IP
        data = self.memory.read(self.registers.AR)
        command, data = self.commandParser(data)
        self.APU(command, data)
        while command!="hlt":
            self.registers.IP += 1
            self.registers.AR = self.registers.IP
            data = self.memory.read(self.registers.AR)
            command, data = self.commandParser(data)
            self.APU(command, data)
