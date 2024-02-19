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


#if else statement to handle the choices 
        
        if choice == "1":
            name = input("Enter your name:")
            if name in accounts:
                print("Account already exists")
            else: 
                accounts[name] = (CheckingAccount(name), SavingsAccount(name))
                print("Account created successfully.")
                print(accounts)
        elif choice =="2":
            name = input("Enter your name:")
            if name in accounts:
                checking_account, savings_account = accounts[name]
                print(f"Welcome back, {name}!")
                print(accounts)
                while True:
                    print("Which account would you like to use: \n 1. Checking \n 2. Savings")
                    # print("1. Checking Balance")
                    # print("2. Savings Balance")
                    # print("3. Deposit Checking")
                    # print("4. Deposit Savings")
                    # print("5. Withdraw Checking")
                    # print("6. Withdraw Savings")
                    # print("7. Logout")

                    option= input("Enter your option:")

                    if option == "1":
                        account= checking_account
                        print("You have selected Checking")
                        print("What would you like to do today?")
                        checking_option=input("1. Withdraw\n2. Deposit\n3. Check balance: ")
                    

                        if checking_option == "1":
                            amount = float(input("Enter the amount you wish to withdraw: "))
                            account.withdraw(amount)
                        if checking_option == "2":
                            amount = float(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        if checking_option == "3":
                            account.check_balance()
                        else:
                            pass
                          

                    elif option == "2":
                        account= savings_account
                        print("You have selected Savings")
                        print("What would you like to do today?")
                        savings_option=input("1. Withdraw\n2. Deposit\n3. Check balance: ")
            
                    
                        if savings_option == "1":
                            amount = float(input("Enter the amount you wish to withdraw: "))
                            account.withdraw(amount)
                        if savings_option == "2":
                            amount = float(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        if savings_option == "3":
                            account.check_balance()
                    
            else: 
                print("Please select either 1 or 2")

                    # if account == CheckingAccount:
                    #     print("What you like to do today?")
                    #     checking_option= input("1. Withdraw \n 2. Deposit \n 3. Check balance")

                    #     if checking_option== "1":
                    #         amount = float(input("Enter the amount you wish to withdraw"))
                    #         account.withdraw(amount)
                    #     if checking_option== "2":
                    #          amount = float(input("Enter the amount to deposit"))
                    #          account.deposit(amount)
                    #     if checking_option== "3":
                    #         account.check_balance(amount)


        
        #             elif option == "3":
        #                 amount = float(input("Enter the amount you wish to withdraw"))
        #                 account.withdraw(amount)
        #             elif option == "4":
        #                 print("you are logged out")
        #                 break
        #             else: 
        #                 print("Not an option try again")
        #     else:
        #         print("Account not found. You will need to create an account first")
        # elif choice =="3":
        #     print("Thank you for using the Bank of Python")
        #     break
        # else:
        #     print("Invalid choice. Pleasw try again")


if __name__ == "__main__":
    main()
    



                

    
        
