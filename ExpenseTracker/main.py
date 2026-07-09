from tracker import ExpenseTracker


MENU = """
=========================================
          Expense Tracker
=========================================

1. Add Income
2. Add Expense
3. View Transactions
4. Find Transaction
5. Delete Transaction

6. Monthly Summary
7. Category Summary
8. Highest Expense
9. Recent Transactions

10. Save Transactions
11. Load Transactions

12. Exit

=========================================
"""


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.\n")


def get_float(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid amount.\n")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.\n")


if __name__ == "__main__":

    tracker = ExpenseTracker()

    # Auto load previous transactions
    tracker.load_transactions()

    while True:

        print(MENU)

        choice = get_int("Enter your choice: ")

        match choice:

            # ---------------- Income ---------------- #

            case 1:
                print("\n===== Add Income =====")

                amount = get_float("Amount: ")
                category = get_non_empty("Category: ")
                description = input("Description: ")

                success, message = tracker.add_transaction(
                    "income",
                    amount,
                    category,
                    description
                )

                print(message)

            # ---------------- Expense ---------------- #

            case 2:
                print("\n===== Add Expense =====")

                amount = get_float("Amount: ")
                category = get_non_empty("Category: ")
                description = input("Description: ")

                success, message = tracker.add_transaction(
                    "expense",
                    amount,
                    category,
                    description
                )

                print(message)

            # ---------------- View ---------------- #

            case 3:

                success, transactions = tracker.view_transactions()

                if success:
                    print()

                    for transaction in transactions:
                        print(transaction)
                        print()

                else:
                    print(transactions)

            # ---------------- Find ---------------- #

            case 4:

                transaction_id = get_int("Transaction ID: ")

                success, result = tracker.find_transaction(transaction_id)

                if success:
                    print()
                    print(result)
                else:
                    print(result)

            # ---------------- Delete ---------------- #

            case 5:

                transaction_id = get_int("Transaction ID: ")

                success, message = tracker.delete_transaction(transaction_id)

                print(message)

            # ---------------- Monthly Summary ---------------- #

            case 6:

                month = get_int("Month (1-12): ")
                year = get_int("Year: ")

                success, summary = tracker.monthly_summary(month, year)

                if success:

                    print("\n========== Monthly Summary ==========")

                    print(f"Income   : ₹{summary['income']:,.2f}")
                    print(f"Expense  : ₹{summary['expense']:,.2f}")
                    print(f"Balance  : ₹{summary['balance']:,.2f}")

                else:
                    print(summary)

            # ---------------- Category Summary ---------------- #

            case 7:

                success, summary = tracker.category_summary()

                if success:

                    print("\n========== Category Summary ==========")

                    for category, amount in summary.items():
                        print(f"{category:<15} ₹{amount:,.2f}")

                else:
                    print(summary)

            # ---------------- Highest Expense ---------------- #

            case 8:

                success, result = tracker.highest_expense()

                if success:
                    print("\nHighest Expense\n")
                    print(result)
                else:
                    print(result)

            # ---------------- Recent Transactions ---------------- #

            case 9:

                success, transactions = tracker.recent_transactions()

                if success:
                    print()

                    for transaction in transactions:
                        print(transaction)
                        print()

                else:
                    print(transactions)

            # ---------------- Save ---------------- #

            case 10:

                success, message = tracker.save_transactions()

                print(message)

            # ---------------- Load ---------------- #

            case 11:

                success, message = tracker.load_transactions()

                print(message)

            # ---------------- Exit ---------------- #

            case 12:

                tracker.save_transactions()

                print("\nTransactions saved.")
                print("Thank you for using Expense Tracker!")

                break

            case _:

                print("Invalid Choice.\n")