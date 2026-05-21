# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')

from src.cart import ShoppingCart
from src.decorators.tax_decorator import TaxDecorator
from src.decorators.shipping_decorator import ShippingDecorator

class OrderFacade:
    def __init__(self):
        self._cart = ShoppingCart()

    def add_item(self, name, price, quantity):
        self._cart.add_item(name, price, quantity)

    def apply_discount(self, code):
        self._cart.apply_discount(code)

    def checkout(self, include_tax=True, include_shipping=True):
        cart = self._cart
        if include_tax:
            cart = TaxDecorator(cart)
        if include_shipping:
            cart = ShippingDecorator(cart)
        cart.print_receipt()
