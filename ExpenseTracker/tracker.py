from collections import defaultdict
from database import Database
from transaction import Transaction


class ExpenseTracker:

    def __init__(self):
        self.db = Database()
        self.next_transaction_id = self.db.get_next_transaction_id()

    # --------------------------------------------------
    # CRUD Operations
    # --------------------------------------------------

    def add_transaction(self, transaction_type, amount, category, description):
        try:
            transaction = Transaction(
                self.next_transaction_id,
                transaction_type,
                amount,
                category,
                description,
            )

            self.db.insert_transaction(transaction)
            self.next_transaction_id += 1

            return True, transaction

        except ValueError as e:
            return False, str(e)

    def view_transactions(self, transaction_type=None, category=None):

        transactions = self.db.get_all_transactions()

        if not transactions:
            return False, "No transactions found."

        if transaction_type:
            transaction_type = transaction_type.lower()

        if category:
            category = category.title()

        filtered = []

        for transaction in transactions:

            if transaction_type and transaction.transaction_type != transaction_type:
                continue

            if category and transaction.category != category:
                continue

            filtered.append(transaction)

        if not filtered:
            return False, "No matching transactions found."

        return True, filtered

    def find_transaction(self, transaction_id):

        transaction = self.db.get_transaction(transaction_id)

        if transaction is None:
            return False, "Transaction not found."

        return True, transaction

    def delete_transaction(self, transaction_id):

        success, result = self.find_transaction(transaction_id)

        if not success:
            return False, result

        self.db.delete_transaction(transaction_id)

        return True, "Transaction deleted successfully."

    # --------------------------------------------------
    # Properties
    # --------------------------------------------------

    @property
    def total_balance(self):

        transactions = self.db.get_all_transactions()

        return sum(
            transaction.signed_amount
            for transaction in transactions
        )

    # --------------------------------------------------
    # Reports
    # --------------------------------------------------

    def overall_summary(self):

        transactions = self.db.get_all_transactions()

        if not transactions:
            return False, "No transactions found."

        income = 0
        expense = 0

        for transaction in transactions:

            if transaction.transaction_type == "income":
                income += transaction.amount
            else:
                expense += transaction.amount

        return True, {
            "income": income,
            "expense": expense,
            "balance": income - expense,
            "transactions": len(transactions),
        }

    def monthly_summary(self, month, year):

        if not 1 <= month <= 12:
            return False, "Invalid month."

        transactions = self.db.get_all_transactions()

        income = 0
        expense = 0

        for transaction in transactions:

            if (
                transaction.date.month == month
                and transaction.date.year == year
            ):

                if transaction.transaction_type == "income":
                    income += transaction.amount
                else:
                    expense += transaction.amount

        return True, {
            "income": income,
            "expense": expense,
            "balance": income - expense,
        }

    def category_summary(self):

        transactions = self.db.get_all_transactions()

        summary = defaultdict(float)

        for transaction in transactions:

            if transaction.transaction_type == "expense":
                summary[transaction.category] += transaction.amount

        return True, dict(summary)

    def highest_expense(self):

        transactions = self.db.get_all_transactions()

        expenses = [
            transaction
            for transaction in transactions
            if transaction.transaction_type == "expense"
        ]

        if not expenses:
            return False, "No expense transactions found."

        return True, max(
            expenses,
            key=lambda transaction: transaction.amount
        )

    def recent_transactions(self, limit=5):

        transactions = self.db.get_all_transactions()

        if not transactions:
            return False, "No transactions found."

        transactions = sorted(
            transactions,
            key=lambda transaction: transaction.date,
            reverse=True
        )

        return True, transactions[:limit]