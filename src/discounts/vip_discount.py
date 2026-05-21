from discounts.base_discount import Discount

class VipDiscount(Discount):

    def apply_discount(self, total):
        return total * 0.50