# -*- coding: utf-8 -*-
from src.decorators.cart_decorator import CartDecorator

class TaxDecorator(CartDecorator):
    def __init__(self, cart, tax_rate=0.18):
        super().__init__(cart)
        self._tax_rate = tax_rate

    def calculate_total(self):
        total = self._cart.calculate_total()
        return total * (1 + self._tax_rate)

    def print_receipt(self):
        self._cart.print_receipt()
        print('KDV (%18): ' + str(round(self._cart.calculate_total() * self._tax_rate, 2)) + ' TL')
        print('KDV DAHIL TOPLAM: ' + str(round(self.calculate_total(), 2)) + ' TL')
