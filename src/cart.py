# -*- coding: utf-8 -*-
from src.discounts.discount_factory import DiscountFactory

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = None
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, event, data):
        for observer in self._observers:
            observer.update(event, data)

    def add_item(self, name, price, quantity):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})
        self.notify_observers('item_added', {'name': name, 'price': price, 'quantity': quantity})

    def apply_discount(self, code):
        self.discount = DiscountFactory.get_discount(code)
        self.notify_observers('discount_applied', {'code': code})

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
