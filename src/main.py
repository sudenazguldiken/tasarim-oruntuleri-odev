# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')

from src.facade import OrderFacade

order = OrderFacade()
order.add_item('Laptop', 15000, 1)
order.add_item('Mouse', 250, 2)
order.apply_discount('STUDENT10')
order.checkout()
