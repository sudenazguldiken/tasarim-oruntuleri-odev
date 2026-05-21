# -*- coding: utf-8 -*-
from src.decorators.cart_decorator import CartDecorator

class ShippingDecorator(CartDecorator):
    def __init__(self, cart, shipping_cost=50):
        super().__init__(cart)
        self._shipping_cost = shipping_cost

    def calculate_total(self):
        return self._cart.calculate_total() + self._shipping_cost

    def print_receipt(self):
        self._cart.print_receipt()
        print('KARGO: ' + str(self._shipping_cost) + ' TL')
        print('KARGO DAHIL TOPLAM: ' + str(self.calculate_total()) + ' TL')
