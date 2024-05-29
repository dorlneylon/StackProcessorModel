

from typing import Any
import json
import Operations.IntMath as IntMath
import Operations.FloatMath as FloatMath
import Operations.BoolMath as BoolMath 
import StackHandler as StackHandler
import DataType as DataType
import Stack as Stack
import IO as IO

class APU():
    def __init__(self, memory, registers, stack = Stack()):
        self.commands = []
        # open json file opcode_set.json and read it to self.commands
        self.commands = json.parse(open("opcode_set.json", "r").read())
        open("opcode_set.json", "r").read()
        self.volume = 0
        self.integer_apu = IntMath(self.commands["integer_operations"])
        self.float_apu = FloatMath(self.commands["float_operations"])
        self.bool_apu = BoolMath(self.commands["bool_operations"])
        self.stack = stack
        self.stack_handler = StackHandler(stack)
        self.IO_apu = IO()
        self.memory_handler = memory
        self.registers = registers
    def __call__(self, command: Any, data: Any) -> Any:
        if command in self.commands["integer_operations"]:
            return self.integer_apu(command, data)
        if command in self.commands["float_operations"]:
            return self.float_apu(command, data)
        if command in self.commands["bool_operations"]:
            return self.bool_apu(command, data)
        if command in self.commands["stack_operations"]:
        # "dup", "swap"
            if command == "dup":
                self.stack_handler.dub()
            if command == "swap":
                self.stack_handler.swap()
        if command in self.commands["IO_operations"]:
            if command == "out":
                self.IO_apu("out"+data, self.stack_handler.peek())
            if command == "in":
                self.stack_handler.push(self.IO_apu("in"+data))
        if command in self.commands["memory_operations"]:
            if command == "ld":
                self.registers.AR_write(data)
                self.stack_handler.push(self.memory_handler.read(data))
            if command == "st":
                self.registers.AR_write(data)
                x = DataType("Data", None, self.stack_handler.peek())
                self.memory_handler.write(self.registers.AR, x)
            if command == "stpop":
                self.registers.AR_write(data)
                x = DataType("Data", None, self.stack_handler.peek())
                self.memory_handler.write(self.registers.AR, x)
                self.stack_handler.pop()
        if command in self.commands["workflow_operations"]:
            if command == "jmp":
                self.registers.IP_write(data)
            if command == "bpos":
                if self.stack_handler.peek() > 0:
                    self.registers.IP_write(data)
            # TODO implement other operations

        


                 
            


            