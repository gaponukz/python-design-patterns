from entities import (
    IWriter,
    ConsoleWriter,
    TxtFileWriter
)

class Service:
    def __init__(self, writer: IWriter):
        '''
        Bridge pattern uses dependency injection
        '''
        self.writer = writer
    
    def do_stuff(self, data):
        self.writer.write(f"{data.__class__.__name__}-ing")

if __name__ == "__main__":
    console = ConsoleWriter()
    file_writer = TxtFileWriter("data.txt")

    Service(console).do_stuff("Hi")
    Service(file_writer).do_stuff("Hi")
