import uuid
class Account:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"
    
class Bank:
    def __init__(self):
        self.accounts={}
    def generator(self):
        return str(uuid.uuid4()) #generates new account number
    def create_account(self, name, initial_deposit):
        account_number = self.generator()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number]= new_account
        self.save_to_file()
    def view_account(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else: print("Account not found")
    def deposit(self, account_number, amount):
        account = self.accounts[account_number]
        account.balance +=amount
        self.save_to_file()
        print("Amount has been added!")
    def withdraw(self, account_number,amount):
        if amount<= self.accounts[account_number].balance:
            account = self.accounts[account_number]
            account.balance -=amount
            self.save_to_file()
            print("Amount has been withdrawn!")
        else:
            print("Not enough funds!")
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            for account in self.accounts.values():
                file.write(f"{account.__str__()}\n")
    def load_from_file(self):
        with open("accounts.txt", "r")as file:
            print(file.read())
        

with open("accounts.txt", "w") as file:
    pass

def main():
    print(f"{'*'*10}Welcome to Bank Application{'*'*10}")
    print("Option 1: Create a new user account!\n\
          Option 2: View an existing account!\n\
          Option 3: Deposit!\n\
          Option 4: Withdraw!\n\
          Option 5: Load accounts from the file!\n\
          Option 6: Exit!")
    option = int(input("Choose an option: "))
    bank = Bank()

    while (option<6):
        if option==1:
            name = input("Name: ")
            try:
                initial_deposit = int(input("Initial deposit: "))
            except ValueError:
                initial_deposit = int(input("Please enter positive integer: "))
            while(initial_deposit<0):
                initial_deposit = int(input("Initial deposit cannot be negative number: "))
            bank.create_account(name=name, initial_deposit=initial_deposit)
        elif option==2:
            account_number = input("Account number: ")
            bank.view_account(account_number=account_number)
        elif option==3:
            account_number = input("Account number: ")
            try:
                amount = int(input("Amount: "))
            except ValueError:
                amount = int(input("Please enter positive integer: "))
            while(amount<0):
                amount = int(input("Amount cannot be negative number: "))
            bank.deposit(account_number=account_number, amount=amount)
        elif option==4:
            account_number = input("Account number: ")
            try:
                amount = int(input("Amount: "))
            except ValueError:
                amount = int(input("Please enter positive integer: "))
            while(amount<0):
                amount = int(input("Amount cannot be negative number: "))
            bank.withdraw(account_number=account_number, amount=amount)
        elif option==5:
            bank.load_from_file()
        option = int(input("Choose an option: "))
main()