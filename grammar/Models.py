import enum

class VarType(enum.Enum):
    ID = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    BOOLEAN = 5
    UNKNOWN = 6


class Value:
    def __init__(self, name, type, length):
        self.name = name
        self.type = type
        self.length = 0
        if length is not None:
            self.length = length
        self.function = ""

    def __str__(self):
        return f'Value: {self.type} = ' + f'{self.name}'



