
class BankAccount:
    interest_rate = 0.02
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                return "retiro exitoso"