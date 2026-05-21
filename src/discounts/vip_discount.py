from discounts.base_discount import Discount

class VipDiscount(Discount):
    def apply(self, total):
        return total * 0.50
