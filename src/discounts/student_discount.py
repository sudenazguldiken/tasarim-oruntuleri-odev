from discounts.base_discount import Discount

class StudentDiscount(Discount):
    def apply(self, total):
        return total * 0.90
