import abc

class IWriter(abc.ABC):
    @abc.abstractmethod
    def write(self, data): ...

class ConsoleWriter(IWriter):
    def write(self, data):
        print(data)

class TxtFileWriter(IWriter):
    def __init__(self, filename: str):
        self.filename = filename
    
    def write(self, data):
        with open(f"{self.filename}", 'a', encoding='utf-8') as out:
            out.write(f"{data}\n")
