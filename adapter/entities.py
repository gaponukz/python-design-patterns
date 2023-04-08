import abc
import typing
import dataclasses

SizeSymbol = typing.Literal['xs', 's', 'm', 'l', 'xl']
Size: typing.TypeAlias = int

class ValueAble(abc.ABC):
    @abc.abstractmethod
    def get_price(self) -> float: ...

class INikeProduct(ValueAble):
    @abc.abstractmethod
    def get_size(self) -> Size: ...

class IAdidasProduct(ValueAble):
    @abc.abstractmethod
    def get_size_symbol(self) -> SizeSymbol: ...

@dataclasses.dataclass
class NikeShirt(INikeProduct):
    price: float
    size: Size

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

@dataclasses.dataclass
class AdidasShirt(IAdidasProduct):
    price: float
    size: SizeSymbol

    def get_price(self):
        return self.price

    def get_size_symbol(self):
        return self.size
