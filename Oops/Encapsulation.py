class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance

    # Getter method for account holder
    def get_account_holder(self):
        return self._account_holder

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # Setter method for balance
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Invalid balance. Balance cannot be negative.")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount} dollars. New balance: {self._balance}")
        else:
            print("Invalid amount for deposit.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount} dollars. New balance: {self._balance}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")


# Creating an instance of BankAccount
account1 = BankAccount("John Doe", 1000)

# Accessing account holder and balance using getter methods
print("Account Holder:", account1.get_account_holder())
print("Current Balance:", account1.get_balance())

# Depositing and withdrawing money
account1.deposit(500)
account1.withdraw(200)

# Trying to set a negative balance using the setter method
account1.set_balance(-100)
