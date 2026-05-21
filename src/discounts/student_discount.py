from discounts.base_discount import Discount

class StudentDiscount(Discount):

    def apply_discount(self, total):
        return total * 0.90