class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        
    def deposit(self, bank, amount):
        bank.deposit(amount)
        
    def withdraw(self, bank, amount):
        bank.withdraw(amount)
        
    def check_balance(self, bank):
        bank.check_balance()

class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account. New balance is {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account. New balance is {self.balance}")
        
    def check_balance(self):
        print(f"Account balance for {self.name} is {self.balance}")


# create bank account
bank = Bank("John Doe", 1000)

# create customer account
customer = Customer("Jane Smith", 123456)

# deposit money
customer.deposit(bank, 500)

# withdraw money
customer.withdraw(bank, 200)

# check balance
customer.check_balance(bank)
