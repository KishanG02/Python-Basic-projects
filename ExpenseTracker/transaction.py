from datetime import datetime


class Transaction:

    VALID_TYPES = {"income", "expense"}

    VALID_CATEGORIES = {
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Salary",
        "Investment",
        "Entertainment",
        "Healthcare",
        "Education",
        "Other"
    }

    def __init__(
        self,
        transaction_id,
        transaction_type,
        amount,
        category,
        description=""
    ):

        self.transaction_id = int(transaction_id)

        transaction_type = transaction_type.lower()

        if transaction_type not in self.VALID_TYPES:
            raise ValueError(
                "Transaction type must be 'income' or 'expense'."
            )

        self.transaction_type = transaction_type

        amount = float(amount)

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        self.amount = amount

        category = category.title()

        if category not in self.VALID_CATEGORIES:
            raise ValueError("Invalid category.")

        self.category = category

        self.description = (
            description.strip()
            if description.strip()
            else "No Description"
        )

        self.date = datetime.now()

    # --------------------------------------------------

    @property
    def signed_amount(self):

        if self.transaction_type == "income":
            return self.amount

        return -self.amount

    # --------------------------------------------------

    def to_dict(self):

        return {
            "id": self.transaction_id,
            "type": self.transaction_type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat()
        }

    # --------------------------------------------------

    @classmethod
    def from_dict(cls, data):

        transaction = cls(
            data["id"],
            data["type"],
            data["amount"],
            data["category"],
            data["description"]
        )

        transaction.date = datetime.fromisoformat(
            data["date"]
        )

        return transaction

    # --------------------------------------------------

    def __str__(self):

        status = "🟢 Income" if self.transaction_type == "income" else "🔴 Expense"

        return (
            f"\n{'='*50}\n"
            f"Transaction ID : {self.transaction_id}\n"
            f"Date           : {self.date.strftime('%d-%m-%Y %H:%M')}\n"
            f"Type           : {status}\n"
            f"Category       : {self.category}\n"
            f"Amount         : ₹{self.amount:,.2f}\n"
            f"Description    : {self.description}\n"
            f"{'='*50}"
        )