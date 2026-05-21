# -*- coding: utf-8 -*-
from discounts.discount_factory import DiscountFactory

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = None

    def add_item(self, name, price, quantity):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def apply_discount(self, code):
        self.discount = DiscountFactory.get_discount(code)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']

        if self.discount:
            total = self.discount.apply(total)

        return total

    def print_receipt(self):
        print('===== FIS =====')
        for item in self.items:
            print(item['name'] + ' x' + str(item['quantity']) + ' = ' + str(item['price'] * item['quantity']) + ' TL')
        print('TOPLAM: ' + str(self.calculate_total()) + ' TL')

cart = ShoppingCart()
cart.add_item('Laptop', 15000, 1)
cart.add_item('Mouse', 250, 2)
cart.apply_discount('STUDENT10')
cart.print_receipt()
