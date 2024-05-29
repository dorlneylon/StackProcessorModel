import DataType

class CommandParser:
    def __init__(self):
        pass
    def __call__(self, command):
        if isinstance(command, DataType.DataType):
            if command.type == "Data":
                return "None", command.data
            else:
                return command.command, command.data
        else:
            #todo
            return "None", 0
        
