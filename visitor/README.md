# Visitor
is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.
The Visitor interface declares a set of visiting methods that can take concrete elements of an object structure as arguments. These methods may have the same names if the program is written in a language that supports overloading, but the type of their parameters must be different.

```py
    def visit(self, item: ItemElement) -> Price:
        cost = 0.0

        if isinstance(item, Pizza):
            cost = item.get_price()
            cost -= cost * 0.15
        
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        
        return cost
```
