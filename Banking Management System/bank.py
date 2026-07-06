import json
from account import BankAccount

class Bank:
    def __init__(self):
        self.accounts = {}
        self.nxt_account_number = 1001

    def create_account(self, name):
            account = BankAccount(name, self.nxt_account_number)
            self.accounts[self.nxt_account_number] = account
            print(f"your Account no.: {self.nxt_account_number}\nYour Account has been created successfully.")
            self.nxt_account_number += 1

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit_money(self, amount, account_number):
        account = self.find_account(account_number)
        if account is None:
            return "Account doesn't Exists."

        if account.deposit(amount):
            print(f"₹{amount} is deposited to the account {account_number}.\nBalance : ₹{account.show_balance()}")
            
    def withdraw_money(self, amount, account_number):
        account = self.find_account(account_number)
        if account is None:
            print("Account Not Found")
            return
        
        if account.withdraw(amount):
            print(f"Withdrawal successful.\nBalance : ₹{account.show_balance()}")


    def check_balance(self, account_number):
        account = self.find_account(account_number)

        if account is None:
            print("Account not found.")
            return

        account.show_balance()

    def transaction_history(self, account_number):
        account = self.find_account(account_number)
        
        if account is None:
            print("Account not found.")
            return
        account.show_history()


    def view_all(self):
        print(f"{'Account No.':<15}{'Name':<15}{'Balance'}")
        print("-"*30)
        for acc_no, info in self.accounts.items():
            print(f"{acc_no:<15}{info.name:<15}{info.balance}")

    def transfer_money(self, amount, from_account_number,to_account_number):
        sender = self.find_account(from_account_number)
        receiver = self.find_account(to_account_number)
        if from_account_number == to_account_number:
            print("Cannot transfer to the same account.")
            return

        if sender is None or receiver is None:
            return
        
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print("Transfer Successful.")

    def save_accounts(self):
        data = {}
        for acc_no, account in self.accounts.items():
            data[acc_no] = account.to_dict()

        with open("Bank_Accounts.json", "w", encoding= "utf-8") as f:
            json.dump(data, f, indent=4)
        print("Account details Saved.")

    def load_accounts(self):
        try:
            with open("Bank_Accounts.json", 'r', encoding = "utf-8") as f:
                data = json.load(f)
            self.accounts = {}

            for account_number, account_data in data.items():
                self.accounts[int(account_number)] = BankAccount.from_dict(account_data)

            if self.accounts:
                self.nxt_account_number = max(self.accounts.keys()) + 1
            else:
                self.nxt_account_number = 1001 
            print("Accounts load Successfully.")

        except FileNotFoundError:
            print("No Bank accounts")
