import sqlite3
from transaction import Transaction


class Database:

    def __init__(self, db_name="expenses.db"):
        self.connection = sqlite3.connect(
            db_name,
            check_same_thread=False
        )
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.create_table()

    # ----------------------------------------------------
    # Create Table
    # ----------------------------------------------------

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions(

                id INTEGER PRIMARY KEY,

                type TEXT NOT NULL,

                amount REAL NOT NULL,

                category TEXT NOT NULL,

                description TEXT,

                date TEXT NOT NULL

            )
        """)

        self.connection.commit()

    # ----------------------------------------------------
    # Create
    # ----------------------------------------------------

    def insert_transaction(self, transaction: Transaction):

        self.cursor.execute("""

            INSERT INTO transactions
            (
                id,
                type,
                amount,
                category,
                description,
                date
            )

            VALUES (?, ?, ?, ?, ?, ?)

        """, (

            transaction.transaction_id,
            transaction.transaction_type,
            transaction.amount,
            transaction.category,
            transaction.description,
            transaction.date.isoformat()

        ))

        self.connection.commit()

    # ----------------------------------------------------
    # Read All
    # ----------------------------------------------------

    def get_all_transactions(self):

        self.cursor.execute("""

            SELECT *
            FROM transactions

            ORDER BY date DESC

        """)

        rows = self.cursor.fetchall()

        transactions = []

        for row in rows:
            transactions.append(
                Transaction.from_dict(dict(row))
            )

        return transactions

    # ----------------------------------------------------
    # Read One
    # ----------------------------------------------------

    def get_transaction(self, transaction_id):

        self.cursor.execute("""

            SELECT *

            FROM transactions

            WHERE id = ?

        """, (transaction_id,))

        row = self.cursor.fetchone()

        if row is None:
            return None

        return Transaction.from_dict(dict(row))

    # ----------------------------------------------------
    # Delete
    # ----------------------------------------------------

    def delete_transaction(self, transaction_id):

        self.cursor.execute("""

            DELETE

            FROM transactions

            WHERE id = ?

        """, (transaction_id,))

        self.connection.commit()

    # ----------------------------------------------------
    # Next ID
    # ----------------------------------------------------

    def get_next_transaction_id(self):

        self.cursor.execute("""

            SELECT MAX(id)

            FROM transactions

        """)

        result = self.cursor.fetchone()[0]

        if result is None:
            return 1

        return result + 1

    # ----------------------------------------------------
    # Summary Queries
    # ----------------------------------------------------

    def get_income(self):

        self.cursor.execute("""

            SELECT
                COALESCE(SUM(amount),0)

            FROM transactions

            WHERE type='income'

        """)

        return self.cursor.fetchone()[0]

    def get_expense(self):

        self.cursor.execute("""

            SELECT
                COALESCE(SUM(amount),0)

            FROM transactions

            WHERE type='expense'

        """)

        return self.cursor.fetchone()[0]

    def get_recent_transactions(self, limit=5):

        self.cursor.execute("""

            SELECT *

            FROM transactions

            ORDER BY date DESC

            LIMIT ?

        """, (limit,))

        rows = self.cursor.fetchall()

        return [
            Transaction.from_dict(dict(row))
            for row in rows
        ]

    # ----------------------------------------------------
    # Close
    # ----------------------------------------------------

    def close(self):
        self.connection.close()