import abc

from entities import IShirt
from entities import IPants

from entities import (
    AdidasShirt,
    AdidasPants,
    NikeShirt,
    NikePants
)

class IClothingStore(abc.ABC):
    @abc.abstractmethod
    def create_shirt(self) -> IShirt: ...

    @abc.abstractmethod
    def create_pants(self) -> IPants: ...

class AdidasStore(IClothingStore):
    def create_shirt(self) -> IShirt:
        return AdidasShirt()
    
    def create_pants(self) -> IPants:
        return AdidasPants()

class NikeStore(IClothingStore):
    def create_shirt(self) -> IShirt:
        return NikeShirt()
    
    def create_pants(self) -> IPants:
        return NikePants()
