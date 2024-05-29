from typing import Any


class DataType:
    def __init__(self, type="Data", command=None, data=None):
        self.type = type
        self.command = command
        self.data = data
    def __call__(self, type, command, data):
        if type == "Command":
            self.type = "Command"
            self.command = command
            self.data = data
        if type == "Data":
            self.type = "Data"
            self.command = "None"
            self.data = data
    def pure(self) -> Any:
        return self.data