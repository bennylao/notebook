class ShoppingCart:
    def __init__(self):
        self.item_list = []
        self.total_price = 0

    def add_item(self, item, price):
        self.item_list.append(item)
        self.total_price += price

    def remove_item(self, item, price):
        self.item_list.remove(item)
        self.total_price -= price

s = ShoppingCart()
s.add_item("apple", 10)
s.add_item("banana", 10)
s.remove_item("apple", 10)

print(s.item_list)