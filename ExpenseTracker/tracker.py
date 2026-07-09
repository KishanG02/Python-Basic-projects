from collections import defaultdict
import csv
from datetime import datetime, date
from transaction import Transaction

class ExpenseTracker:

    def __init__(self):
        self.transactions = {}
        self.next_transaction_id = 1

    def add_transaction(self, transaction_type, amount, category, description):
        try:
            transaction = Transaction(self.next_transaction_id, transaction_type, amount, category, description)
        except ValueError as e:
            return False, str(e)
        else:
            self.transactions[self.next_transaction_id] = transaction
            self.next_transaction_id += 1 
            return True, transaction

    def view_transactions(self, transaction_type = None, category = None):
        if not self.transactions:
            return False, "No transactions found."

        category = category.title() if category else None

        transaction_type = transaction_type.lower() if transaction_type else None

        filtered = []
        for transaction in self.transactions.values():
            if category and transaction.category != category:
                continue
            if transaction_type and transaction.transaction_type != transaction_type:
                continue
            filtered.append(transaction)

        if not filtered:
            return False, "No matching transactions found."

        return True, filtered


    def delete_transaction(self, transaction_id):
        success, result = self.find_transaction(transaction_id)
        if not success:
            return False, result
        del self.transactions[transaction_id]
        return True, "Transaction deleted successfully."

    def find_transaction(self, transaction_id):
        if transaction_id not in self.transactions:
            return False, "No transaction found."
        return True, self.transactions[transaction_id]

    @property
    def total_balance(self):
        return sum(
            transaction.signed_amount
            for transaction in self.transactions.values()
        )

    def overall_summary(self):
        if not self.transactions:
            return False, "No transactions found."

        income = 0
        expense = 0

        for transaction in self.transactions.values():
            if transaction.transaction_type == "income":
                income += transaction.amount
            else:
                expense += transaction.amount

        return True, {
            "income": income,
            "expense": expense,
            "balance": income - expense,
        }

    def monthly_summary(self, month, year):
        if not 1 <= month <= 12:
            return False, "Invalid month."

        income = 0
        expense = 0
        
        for transaction in self.transactions.values():
            if transaction.date.month == month and transaction.date.year == year:
                if transaction.transaction_type == 'income':
                    income += transaction.amount
                else:
                    expense += transaction.amount
    
        return True, {
            "income": income,
            "expense": expense,
            "balance": income - expense,
        }

    def category_summary(self):

        summary = defaultdict(float)

        for transaction in self.transactions.values():
            if transaction.transaction_type == 'expense':
                summary[transaction.category] += transaction.amount

        return True, dict(summary)

    def highest_expense(self):

        filtered = []
        for transaction in self.transactions.values():
            if transaction.transaction_type == 'expense':
                filtered.append(transaction)
        
        if not filtered:
            return False, "No expense transactions found."
        
        return True, max(filtered, key=lambda transaction: transaction.amount)

    def recent_transactions(self, limit = 5):
        if not self.transactions:
            return False, "No transactions found."

        last =  sorted(self.transactions.values(), key= lambda transaction: transaction.date, reverse= True)

        return True, last[:limit]

    def save_transactions(self):
        try:
            with open("transactions.csv", "w", newline="", encoding='utf-8') as f:
                field_name = ['id', 'type', 'amount', 'category', 'description', 'date']
                writer = csv.DictWriter(f, fieldnames= field_name)
                writer.writeheader()

                for transaction in self.transactions.values():
                    writer.writerow(transaction.to_dict())
        except OSError as e:
            return False, str(e)

        return True, "File Saved successfully."

    def load_transactions(self):

        try:
            with open("transactions.csv", "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.transactions ={}
                for row in reader:
                    transaction = Transaction.from_dict(row)
                    self.transactions[transaction.transaction_id] = transaction
                if self.transactions:
                    self.next_transaction_id = max(self.transactions.keys())+1
                else:
                    self.next_transaction_id = 1

        except FileNotFoundError:
            self.transactions = {}
            self.next_transaction_id = 1
            return True, "No saved transactions found."
        except Exception as e:
            return False, str(e)

        return True, "File Loaded successfully."

