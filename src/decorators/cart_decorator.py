# -*- coding: utf-8 -*-
from src.cart import ShoppingCart

class CartDecorator:
    def __init__(self, cart):
        self._cart = cart

    def add_item(self, name, price, quantity):
        self._cart.add_item(name, price, quantity)

    def apply_discount(self, code):
        self._cart.apply_discount(code)

    def calculate_total(self):
        return self._cart.calculate_total()

    def print_receipt(self):
        self._cart.print_receipt()
