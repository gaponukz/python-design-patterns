import abc
import typing

Color = typing.Literal['red', 'green', 'blue', 'yellow', 'black']
SizeSymbol = typing.Literal['xs', 's', 'm', 'l', 'xl']
Size: typing.TypeAlias = int

class IProduct(abc.ABC):
    @abc.abstractmethod
    def get_price(self) -> float: ...

    @abc.abstractmethod
    def get_color(self) -> Color: ...

class IShirt(IProduct):
    @abc.abstractmethod
    def get_size(self) -> SizeSymbol: ...

class IPants(IProduct):
    @abc.abstractmethod
    def get_size(self) -> Size: ...

'''
We will skip logic and just add plugs
'''

class AdidasShirt(IShirt):
    def get_price(self) -> float:
        return 10
    
    def get_color(self) -> Color:
        return "blue"

    def get_size(self) -> SizeSymbol:
        return "m"

class AdidasPants(IPants):
    def get_price(self) -> float:
        return 10
    
    def get_color(self) -> Color:
        return "black"

    def get_size(self) -> Size:
        return 38

class NikeShirt(IShirt):
    def get_price(self) -> float:
        return 12
    
    def get_color(self) -> Color:
        return "green"

    def get_size(self) -> SizeSymbol:
        return "m"

class NikePants(IPants):
    def get_price(self) -> float:
        return 12
    
    def get_color(self) -> Color:
        return "blue"

    def get_size(self) -> Size:
        return 38

