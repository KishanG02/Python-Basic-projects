class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            print("Book is already borrowed.")
            return False
        self.available = False
        return True

    def return_book(self):
        if self.available:
            print("Book is already available.")
            return False
        self.available = True
        return self.available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    def __str__(self):
        status = "Available." if self.available else "Borrowed."

        return (
            f"Book Id : {self.book_id}\n"
            f"Title : {self.title}\n"
            f"Author : {self.author}\n"
            f"status : {status}"
        )

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data['book_id'],
            data['title'],
            data['author']
        )
        book.available = data['available'] == 'True'
        return book