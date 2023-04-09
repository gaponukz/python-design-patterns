# Pizza class that will be built by the Builder
class Pizza:
    def __init__(self):
        self.size = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f"Size: {self.size}\nSauce: {self.sauce}\nToppings: {', '.join(self.toppings)}"

# Builder class that builds the Pizza object
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza

# Director class that directs the building process
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_margherita(self):
        self.builder.set_size("medium")
        self.builder.set_sauce("tomato")
        self.builder.add_topping("cheese")
        return self.builder.build()

    def build_pepperoni(self):
        self.builder.set_size("large")
        self.builder.set_sauce("tomato")
        self.builder.add_topping("cheese")
        self.builder.add_topping("pepperoni")
        return self.builder.build()

# Example usage
builder = PizzaBuilder()
director = PizzaDirector(builder)

margherita = director.build_margherita()
print(margherita)

pepperoni = director.build_pepperoni()
print(pepperoni)
