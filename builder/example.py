from __future__ import annotations

import typing
import dataclasses

PizzaSize = typing.Literal['small', 'medium', 'large']
Sauce = typing.Literal['tomatoes', 'spicy red', 'pesto']
Cheese = typing.Literal['mozzarela', 'cheddar', 'gorgonzola']
Toping = typing.Literal['pepperoni', 'mushrooms', 'onion']

'''
We want to buil app where user can create custom pizza
'''

# Pizza class that will be built by the Builder
@dataclasses.dataclass
class Pizza:
    size: PizzaSize | None = None
    sauce: Sauce | None = None
    toppings: list[Cheese | Toping] = dataclasses.field(default_factory=list)

# Builder class that builds the Pizza object
class PizzaBuilder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pizza = Pizza()

    def set_size(self, size: PizzaSize) -> PizzaBuilder:
        self.pizza.size = size
        return self

    def set_sauce(self, sauce: Sauce) -> PizzaBuilder:
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping: Toping | Cheese) -> PizzaBuilder:
        self.pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        return self.pizza

# Director class that directs the building process
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def build_margherita(self):
        self.builder.set_size("medium")
        self.builder.set_sauce("tomato")
        self.builder.add_topping("mozzarela")
        return self.builder.build()

    def build_pepperoni(self):
        self.builder.set_size("large")
        self.builder.set_sauce("tomato")
        self.builder.add_topping("mozzarela")
        self.builder.add_topping("pepperoni")
        return self.builder.build()

if __name__ == "__main__":
    builder = PizzaBuilder()
    director = PizzaDirector(builder)

    margherita = director.build_margherita()
    print(margherita)

    pepperoni = director.build_pepperoni()
    print(pepperoni)
