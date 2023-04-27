import abc
import typing

Price: typing.TypeAlias = float | int

class IOrderItemVisitor(abc.ABC):
    @abc.abstractmethod
    def visit(self, item: typing.Any) -> Price: ...

class ItemElement(abc.ABC):
    @abc.abstractmethod
    def accept(self, visitor: IOrderItemVisitor) -> Price: ...

class Pizza(ItemElement):
    def __init__(self, name: str, price: Price):
        self.name = name
        self.price = price

    def get_price(self) -> Price:
        return self.price

    def accept(self, visitor: IOrderItemVisitor) -> Price:
        return visitor.visit(self)


class Coffee(ItemElement):
    def __init__(self, name: str, price: Price, capacity: Price):
        self.name = name
        self.price = price
        self.capacity = capacity

    def get_price(self) -> Price:
        return self.price

    def get_capacity(self) -> Price:
        return self.capacity

    def accept(self, visitor: IOrderItemVisitor) -> Price:
        return visitor.visit(self)


class WithOutDiscountVisitor(IOrderItemVisitor):
    def visit(self, item: ItemElement) -> Price:
        cost = 0.0
        
        if isinstance(item, Pizza):
            cost = item.get_price()

        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        
        return cost


class OnlyPizzaDiscountVisitor(IOrderItemVisitor):
    def visit(self, item: ItemElement) -> Price:
        cost = 0.0

        if isinstance(item, Pizza):
            cost = item.get_price()
            cost -= cost * 0.15
        
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        
        return cost


class OnlyCoffeeDiscountVisitor(IOrderItemVisitor):
    def visit(self, item: ItemElement) -> Price:
        cost = 0.0
        
        if isinstance(item, Pizza):
            cost = item.get_price()
        
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
            cost -= cost * 0.35
        
        return cost


class AllDiscountVisitor(IOrderItemVisitor):
    def visit(self, item: ItemElement) -> Price:
        cost = 0.0

        if isinstance(item, Pizza):
            cost = item.get_price()
        
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        
        cost -= cost * 0.20
        return cost

class Waiter:
    def __init__(self, discount: IOrderItemVisitor):
        self.order: list[ItemElement] = []
        self.discount_calculator = discount

    def set_order(self, order: list[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount: IOrderItemVisitor) -> None:
        self.discount_calculator = discount

    def calculate_finish_price(self) -> Price:
        price = 0.0

        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        
        return price

if __name__ == "__main__":
    discount: IOrderItemVisitor
    order: list[ItemElement] = [
        Pizza("Margarita", 12.3),
        Coffee("Latte", 5, 0.3),
        Pizza("4 Raw", 10.5),
        Pizza("Salami", 15.2),
        Coffee("Cappuccino", 4, 0.27)
    ]

    discount = WithOutDiscountVisitor()
    waiter = Waiter(discount)
    waiter.set_order(order)
    print(f"Without discount: {waiter.calculate_finish_price()}")
    
    discount = OnlyPizzaDiscountVisitor()
    waiter.set_discount(discount)
    print(f"With pizza discount: {waiter.calculate_finish_price()}")
    
    discount = OnlyCoffeeDiscountVisitor()
    waiter.set_discount(discount)
    print(f"with coffe discount: {waiter.calculate_finish_price()}")
    
    discount = AllDiscountVisitor()
    waiter.set_discount(discount)
    print(f"With all discount: {waiter.calculate_finish_price()}")
