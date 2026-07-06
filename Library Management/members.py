class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if not book_id:
            return False

        if book_id in self.borrowed_books:
            return False
        self.borrowed_books.append(book_id)
        return True

    def return_book(self, book_id):
        if not book_id:
            return False

        if book_id not in self.borrowed_books:
            return False
        self.borrowed_books.remove(book_id)
        return True

    def __str__(self):
        return (
            f"Member Id: {self.member_id}\n"
            f"Name: {self.name}\n"
            f"Borrowed books: {self.borrowed_books}"
        )

    def to_dict(self):
        return{
            "member_id" : self.member_id,
            "name" : self.name,
            "borrowed_books" : self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            data['member_id'],
            data['name']
        )
        member.borrowed_books = data['borrowed_books'].split('|')
        return member