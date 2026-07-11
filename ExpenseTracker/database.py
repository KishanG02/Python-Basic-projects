import sqlite3
from transaction import Transaction


class Database:

    def __init__(self, db_name="expenses.db"):
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_table()

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

    def insert_transaction(self, transaction: Transaction):
        self.cursor.execute("""
            INSERT INTO transactions
            (id, type, amount, category, description, date)
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

    def get_all_transactions(self):
        self.cursor.execute("""
            SELECT *
            FROM transactions
            ORDER BY date DESC
        """)

        rows = self.cursor.fetchall()

        return [
            Transaction.from_dict(dict(row))
            for row in rows
        ]

    def get_transaction(self, transaction_id):
        self.cursor.execute("""
            SELECT *
            FROM transactions
            WHERE id = ?
        """, (transaction_id,))

        row = self.cursor.fetchone()

        if row:
            return Transaction.from_dict(dict(row))

        return None

    def delete_transaction(self, transaction_id):
        self.cursor.execute("""
            DELETE
            FROM transactions
            WHERE id = ?
        """, (transaction_id,))

        self.connection.commit()

    def clear_transactions(self):
        self.cursor.execute("""
            DELETE FROM transactions
        """)
        self.connection.commit()

    def get_next_transaction_id(self):

        self.cursor.execute(
            "SELECT MAX(id) FROM transactions"
        )

        result = self.cursor.fetchone()[0]

        if result is None:
            return 1

        return result + 1

    def close(self):
        self.connection.close()