class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
            return False
        self.balance += amount 
        self.history.append(f"Deposit +{amount}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid Amount.")
            return False

        if amount > self.balance:
            print("Insufficient balance.")
            return False
            
        self.balance -= amount
        self.history.append(f"Withdraw -{amount}")
        return True

    def to_dict(self):
        return {
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.balance,
            "history": self.history
        }

    @classmethod
    def from_dict(cls, data):
        account = cls(
            data['name'],
            data['account_number'],
            )
        account.balance = data['balance']
        account.history = data['history']
        return account

    def show_balance(self):
        print(f"yuor account balance is ₹{self.balance}")

    def show_history(self):
        if not self.history:
            print("No transactions found.")
            return

        print("\nTransaction History")
        print("-"*30)
        for transaction in self.history:
            print(transaction)

    def __str__(self):
        return (
            f"Account Number : {self.account_number}\n"
            f"Name           : {self.name}\n"
            f"Balance        : ₹{self.balance}"
        )