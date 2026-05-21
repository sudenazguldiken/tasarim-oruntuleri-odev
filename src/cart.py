class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount_code = None

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def apply_discount(self, code):
        self.discount_code = code

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]

        if self.discount_code == "STUDENT10":
            total = total * 0.90
        elif self.discount_code == "SUMMER20":
            total = total * 0.80
        elif self.discount_code == "VIP50":
            total = total * 0.50

        return total

    def print_receipt(self):
        print("===== FİŞ =====")
        for item in self.items:
            print(f"{item['name']} x{item['quantity']} = {item['price'] * item['quantity']} TL")
        print(f"TOPLAM: {self.calculate_total()} TL")


# Test
cart = ShoppingCart()
cart.add_item("Laptop", 15000, 1)
cart.add_item("Mouse", 250, 2)
cart.apply_discount("STUDENT10")
cart.print_receipt()