
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
                print( "retiro exitoso")
            else:
                print('saldo insuficiente')
        else:
            print("error: el monto debe ser mayor a cero")
            
account1 = BankAccount("david", 1000)
print(BankAccount.interest_rate)
print(BankAccount.change_interest_rate(0.03))
print(BankAccount.interest_rate)

account1.withdraw(999)
account1.withdraw(5)