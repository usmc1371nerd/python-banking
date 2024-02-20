from flask import Flask, request

app = Flask(__name__)


#make sure app is connecting to browser by hardcoding the h1 Python Banking app
@app.route('/')
def index():
    return "<h1>Python Banking App<h1>"



class CheckingAccount:
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

class SavingsAccount:
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
        print("Welcome to the Bank of Python")
        print("1. Create Account")
        print("2. Log in")
        print("3. Quit")

        choice = input("Please chose your option:")


#if else statement to handle the choices from user
        
        if choice == "1":
            name = input("Enter your name:")
            if name in accounts:
                print("Account already exists")
            else: 
                accounts[name] = (CheckingAccount(name), SavingsAccount(name))
                print("Account created successfully.")
                print("choice 1")
        elif choice =="2":
            name = input("Enter your name:")
            if name in accounts:
                checking_account, savings_account = accounts[name]
                print(f"Welcome back, {name}!")
                print("this is working")
                while True:
                    print("Which account would you like to use: \n 1. Checking \n 2. Savings \n 3. Back to Main Menu")
                
            
                    option= input("Enter your option:")

                    if option == "1":
                        account= checking_account
                        print("You have selected Checking")
                        print("What would you like to do today?")
                        checking_option=input("1. Withdraw\n2. Deposit\n3. Check balance:")
                            

                        if checking_option == "1":
                            amount = float(input("Enter the amount you wish to withdraw: "))
                            account.withdraw(amount)
                        elif checking_option == "2":
                            amount = float(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        elif checking_option == "3":
                            account.check_balance()          
                    else:
                      pass   

                                
                                
                    if option == "2":
                        account= savings_account
                        print("You have selected Savings")
                        print("What would you like to do today?")
                        savings_option=input("1. Withdraw\n2. Deposit\n3. Check balance: ")
                    
                            
                        if savings_option == "1":
                            amount = float(input("Enter the amount you wish to withdraw: "))
                            account.withdraw(amount)
                        elif savings_option == "2":
                            amount = float(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        elif savings_option == "3":
                            account.check_balance()
                        else:
                            pass
                    elif option == "3":
                        break
        
        elif choice=="3":
            print("You are logged out")
            break                   
                        
       
if __name__ == "__main__":
    app.run(debug=True)
    



                

    
        
