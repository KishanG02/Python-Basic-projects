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

    def __init__(self, transaction_id, transaction_type, amount, category, description):
        self.transaction_id = transaction_id
        if transaction_type.lower() not in self.VALID_TYPES:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        self.transaction_type = transaction_type.lower()
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.amount = amount
        if category.title() not in self.VALID_CATEGORIES:
            raise ValueError("Category must be valid.")
        self.category = category.title()
        self.description = description.strip() or "No description"
        self.date = datetime.now()


    def __str__(self):
        return (
            f"{'='*45}\n"
            f"Transaction #{self.transaction_id}\n"
            f"{'-'*45}\n"
            f"Date : {self.date.strftime('%d-%m-%Y %H:%M')}\n"
            f"Type : {self.transaction_type.title()}\n"
            f"Amount : ₹ {self.amount:,.2f}\n"
            f"Category : {self.category}\n"
            f"Description : {self.description}\n"
            f"{'='*45}"
            )

    def to_dict(self):
        return {
            "id" : self.transaction_id,
            "type" : self.transaction_type,
            "amount" : self.amount,
            "category" : self.category,
            "description" : self.description,
            "date" : self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        record = cls(
            int(data['id']),
            data['type'],
            float(data['amount']),
            data['category'],
            data['description']
        )
        record.date = datetime.fromisoformat(data['date'])

        return record

    @property
    def signed_amount(self):
        return self.amount if self.transaction_type == "income" else -self.amount



