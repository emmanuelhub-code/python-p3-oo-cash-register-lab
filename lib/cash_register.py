# lib/cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0
        self.last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        self.last_transaction_items = [title] * quantity
        self.items.extend(self.last_transaction_items)

    def apply_discount(self):
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        for item in self.last_transaction_items:
            if item in self.items:
                self.items.remove(item)
        self.last_transaction_amount = 0
        self.last_transaction_items = []
