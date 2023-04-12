class ShopFacade:
    def __init__(self, customer_id):
        self._customer_id = customer_id
        self._inventory = Inventory()
        self._discount = Discount()
        self._checkout = Checkout()

    def get_offer(self, item_id):
        item = self._inventory.get_item(item_id)
        item_price = self._discount.apply_discount(item.price, self._customer_id)
        return item.name, item_price

    def checkout_cart(self, cart):
        total_price = sum([self.get_offer(item_id)[1] for item_id in cart])
        return self._checkout.process_payment(self._customer_id, total_price)


class Inventory:
    def __init__(self):
        self._items = {
            1: Item("Shirt", 20.0),
            2: Item("Pants", 30.0),
            3: Item("Shoes", 50.0),
            4: Item("Hat", 10.0),
        }

    def get_item(self, item_id):
        return self._items.get(item_id)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Discount:
    def apply_discount(self, price, customer_id):
        if customer_id == 1:  # VIP customer
            return price * 0.8
        
        elif customer_id == 2:  # Regular customer
            return price * 0.9

        else:
            return price


class Checkout:
    def process_payment(self, customer_id, amount):
        # Here we would actually process the payment through a payment gateway or something similar
        return f"Payment of {amount} processed for customer {customer_id}"


if __name__ == "__main__":
    customer_id = 1
    shop = ShopFacade(customer_id)
    cart = [1, 2, 3]  # IDs of items in the cart
    offer = [shop.get_offer(item_id) for item_id in cart]
    print(offer)  # [('Shirt', 16.0), ('Pants', 27.0), ('Shoes', 40.0)]

    payment_result = shop.checkout_cart(cart)
    print(payment_result)  # Payment of 83.0 processed for customer 1
