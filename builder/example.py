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
        return self.builder\
            .set_size("medium")\
            .set_sauce("tomato")\
            .add_topping("mozzarela")\
            .build()

    def build_pepperoni(self):
        return self.builder\
            .set_size("large")\
            .set_sauce("tomato")\
            .add_topping("mozzarela")\
            .add_topping("pepperoni")\
            .build()

if __name__ == "__main__":
    director = PizzaDirector(PizzaBuilder())

    margherita = director.build_margherita()
    print(margherita)

    pepperoni = director.build_pepperoni()
    print(pepperoni)
