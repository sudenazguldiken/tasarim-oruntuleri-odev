from discounts.base_discount import Discount

class SummerDiscount(Discount):

    def apply_discount(self, total):
        return total * 0.80