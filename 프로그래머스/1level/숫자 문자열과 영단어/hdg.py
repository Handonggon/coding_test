from enum import Enum
class NUMBER(Enum):
    ZERO  = "0"
    ONE   = "1"
    TWO   = "2"
    THREE = "3" 
    FOUR  = "4"
    FIVE  = "5"
    SIX   = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE  = "9"
    
class Enum:
    @staticmethod
    def create(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        for key, value in enums.items():
            infoFn = lambda s: str(value)
            enums[key] = type(key, (), {"__str__": infoFn, "__repr__": infoFn, "name": key})()
        enums["keys"] = list(enums.keys())
        enums["index"] = 0
        enums["__iter__"] = lambda self: self
        def __next__(self):
            if self.index >= len(self.keys):
                self.index = 0
                raise StopIteration
            enum = enums[self.keys[self.index]]
            value = type("t", (), {"name": enum.name, "value": enum})()
            self.index += 1
            return value
        enums["__next__"] = __next__
        return type('Enum', (), enums)()


def solution(s):
    #NUMBER = Enum.create("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
    for number in Color:
        s = s.replace(number.name.lower(), str(number.value))
    return int(s)
