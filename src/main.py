# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')

from src.facade import OrderFacade
from src.observers.stock_observer import StockObserver
from src.observers.notification_observer import NotificationObserver
from src.cart import ShoppingCart
from src.decorators.tax_decorator import TaxDecorator
from src.decorators.shipping_decorator import ShippingDecorator

cart = ShoppingCart()
cart.add_observer(StockObserver())
cart.add_observer(NotificationObserver())

cart.add_item('Laptop', 15000, 1)
cart.add_item('Mouse', 250, 2)
cart.apply_discount('STUDENT10')

cart_with_tax = TaxDecorator(cart)
cart_with_shipping = ShippingDecorator(cart_with_tax)
cart_with_shipping.print_receipt()
