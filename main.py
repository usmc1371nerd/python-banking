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

    def check_balance (self):
        print(f"Your balance is {self.balance} dollars.")


##################################
#                                #
#          USER LOGIC            #
#                                #
##################################

def main():
    accounts={}

    while True:
        print("\nWelcome to the Bank of Python")
        print("1. Create Account")
        print("2. Log in")
        print("3. Quit")

        choice = input("Please chose your option:")


#if else statement to handle the choices 
        
        if choice == "1":
            name = input("Enter your name:")
            if name in accounts:
                print("Account already exists")
            else: 
                accounts[name] = BankAccount(name)
                print("Account created successfully.")
        elif choice =="2":
            name = input("Enter your name:")
            if name in accounts:
                account = accounts[name]
                print(f"Welcome back, {name}!")
                while True:
                    print("\n 1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    option= input("Enter your option:")

                    if option == "1":
                        account.check_balance()
                    elif option == "2":
                        amount = float(input("Enter the amount to deposit"))
                        account.deposit(amount)
                    elif option == "3":
                        amount = float(input("Enter the amount you wish to withdraw"))
                        account.withdraw(amount)
                    elif option == "4":
                        print("you are logged out")
                        break
                    else: 
                        print("Not an option try again")
                    


                

    
        
