from entities import Product

def problem():
    '''
    Our program worked fine but after some time client want to add discount for some products/users.
    Our solution was too terrible...
    '''
    product = Product("Phone", 500)
    price = product.get_price()

    if 'client have bronze discount':
        price *= 0.95
    
    if 'client have silver discount':
        price *= 0.9
    
    ...

    return price

class DiscountDecorator(Product):
    _product: Product = None

    def __init__(self, product: Product, discount: float):
        super().__init__(product.name, product.price) # is not mandatory
        self._product = product
        self.discount = discount
    
    @property
    def product(self):
        return self._product
    
    def get_price(self) -> float:
        return self.product.get_price() * (1 - self.discount)

class BronzeDiscount(DiscountDecorator):
    def __init__(self, product: Product):
        super().__init__(product, 0.05)

class SilverDiscount(DiscountDecorator):
    def __init__(self, product: Product):
        super().__init__(product, 0.1)

class GoldDiscount(DiscountDecorator):
    def __init__(self, product):
        super().__init__(product, 0.15)

def solution():
    '''
    Now we make our solution better and able to add more features.
    OCP/DIP implementation.
    '''
    product = Product("Phone", 500)

    if 'client have bronze discount':
        product = BronzeDiscount(product)
    
    if 'client have silver discount':
        product = SilverDiscount(product)

    ...

    return product.get_price()

if __name__ == '__main__':
    print(problem())
    print(solution())
