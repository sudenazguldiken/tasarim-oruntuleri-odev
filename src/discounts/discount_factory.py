from discounts.student_discount import StudentDiscount
from discounts.summer_discount import SummerDiscount
from discounts.vip_discount import VipDiscount

class DiscountFactory:
    @staticmethod
    def get_discount(discount_code):
        if discount_code == "STUDENT10":
            return StudentDiscount()
        elif discount_code == "SUMMER20":
            return SummerDiscount()
        elif discount_code == "VIP50":
            return VipDiscount()
        else:
            return None