class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositied {amount} dollars. New balance: {self.balance} dollars.")    

    def withdraw (self, amount):
        if amount > self.balance:
            print("Insufficent funds")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} dollars. New balance: {self.balance} dollars.")

    
