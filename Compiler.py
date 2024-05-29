import json
import DataType

class RunFile():
    def __init__(self, file_path):
        # open file and read by lines
        open_file = open(file_path, 'r')
        lines = open_file.readlines()
        open_file.close()
        self.file = lines
    
class Compile():
    def  __init__(self, config="opcode.json"):
        self.commands = []
        self.json = json.load(open(config, 'r'))
        self.commands = self.json['commands']
    def __call__(self, content, first_adr=100):
        self.program = []
        self.words = {}
        self.values = []
        content = content.lower()
        words_counter=first_adr+1
        for line in content:
            line_cont = line.strip().split(" ")
            if len(line_cont)  >  1:
                if line_cont[0] == "word":
                    self.words[line_cont[1].strip()] = words_counter                    
                    info = DataType("Data", None, line_cont[1].strip())
                    self.program.append(info)
                    words_counter+=1
        for line in content:
            line_cont = line.strip().split(" ")
            if len(line_cont) >= 2:
                if line_cont[0] in self.commands:
                    com = line_cont[0]
                    data = line_cont[1]
                    if data in self.words.keys():
                        info = DataType("Command", com, self.words[data])
                        self.program.append(info)
                    else:
                        info = DataType("Command", com, int(data))
                        self.program.append(info)
                else: 
                    pass
            else:
                com = line_cont[0]
                if com in self.commands:
                    info  = DataType("Command", com, None)
                    self.program.append(info)
                else:
                    pass
        self.program = [DataType("Command", None, None)]*first_adr+self.program
        return self.program



                    

                        
                    