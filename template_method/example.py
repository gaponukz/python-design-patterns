import abc
import typing

T = typing.TypeVar('T')

class SellProductTemplate(abc.ABC, typing.Generic[T]):
    @abc.abstractmethod
    def check_if_product_exists(self, product: T) -> bool: ...

    @abc.abstractmethod
    def get_product_price(self, product: T) -> float: ...

    @abc.abstractmethod
    def remove_product(self, product: T): ...

    def sell(self, product: T):
        if self.check_if_product_exists(product):
            print(f"Selling product {product} for {self.get_product_price(product)}$")

            self.remove_product(product)

class ClothesShop(SellProductTemplate[str]):
    def __init__(self):
        self._prices: dict[str, float] = {
            "pants": 10.0,
            "shorts": 8.0
        }
    
    def check_if_product_exists(self, product: str) -> bool:
        return product in self._prices
    
    def get_product_price(self, product: str) -> float:
        return self._prices[product]
    
    def remove_product(self, product: str):
        del self._prices[product]

if __name__ == "__main__":
    shop = ClothesShop()
    shop.sell("pants")
