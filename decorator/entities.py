import abc
import dataclasses

class IProduct(abc.ABC):
    @abc.abstractmethod
    def get_price(self) -> float: ...

@dataclasses.dataclass
class Product(IProduct):
    name: str
    price: float

    def get_price(self) -> float:
        return self.price
