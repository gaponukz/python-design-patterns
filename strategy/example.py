import abc
import dataclasses

class PaymentStrategy(abc.ABC):
    @abc.abstractmethod
    def pay(self, amount: float): ...


class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self._expiration_date = expiration_date
        self._cvv = cvv

    def pay(self, amount: float):
        print(f"Paid ${amount} with Credit Card {self.card_number}")


class PayPalPaymentStrategy(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self._password = password

    def pay(self, amount: float):
        print(f"Paid ${amount} with PayPal account {self.email}")


@dataclasses.dataclass
class Product:
    name: str
    price: float

class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_Product(self, product: Product):
        self.products.remove(product)

    def calculate_total(self) -> float:
        return sum(product.price for product in self.products)

    def checkout(self):
        total = self.calculate_total()
        self.payment_strategy.pay(total)

if __name__ == '__main__':
    Product1 = Product("Product 1", 10.99)
    Product2 = Product("Product 2", 5.99)
    Product3 = Product("Product 3", 2.49)

    credit_card_strategy = CreditCardPaymentStrategy("1234567890123456", "12/24", "123")
    paypal_strategy = PayPalPaymentStrategy("example@example.com", "mypassword")

    cart1 = ShoppingCart(credit_card_strategy)
    cart2 = ShoppingCart(paypal_strategy)

    cart1.add_product(Product1)
    cart1.add_product(Product2)
    cart2.add_product(Product3)

    cart1.checkout()
    cart2.checkout()
