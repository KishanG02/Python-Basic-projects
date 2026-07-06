import csv
from books import Book
from members import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.nxt_book_id = 101
        self.nxt_member_id = 1
        

    def add_book(self, title, author):
        book = Book(self.nxt_book_id, title, author)
        self.books[self.nxt_book_id] = book
        self.nxt_book_id += 1
        print("Book has been added to the library.")
        return True

    def find_book(self, book_id):
        return self.books.get(book_id)

    def search_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print('Book not found.')
            return False
        print(f"{'Book Id':<10}{'Title':<15}{'Author':<15}{'Available'}")
        print('-'*45)
        print(f"{book.book_id :<10}{book.title:<15}{book.author:<15}{book.available}")
        return True

    def remove_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print('Book not found.')
            return False

        if not book.available:
            print("Cannot remove a borrowed book.")
            return False

        del self.books[book_id]
        print('Book removed successfully.')
        return True

    def register_member(self, name):
        member = Member(self.nxt_member_id, name)
        self.members[self.nxt_member_id] = member
        self.nxt_member_id += 1
        print("Member registered successfully.")
        return True

    def find_member(self, member_id):
        return self.members.get(member_id)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member is None:
            print('Member not found.')
            return False
        
        if book is None:
            print('Book not found.')
            return False
        
        if not book.borrow():
            print('Book not available.')
            return False

        if not member.borrow_book(book_id):
            book.return_book()
            return False
            
        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member is None:
            print('Member not found.')
            return False
        
        if book is None:
            print('Book not found.')
            return False

        if book.available:
            print('Book already available.')
            return False
        
        if not member.return_book(book_id):
            print("Member has not borrowed this book.")
            return False

        book.return_book()

        print("Book returned successfully.")
        return True


    def save_books(self):
        
        with open('Books.csv', 'w', newline= "", encoding='utf-8') as f:
            fieldnames = ['book_id','title', 'author', 'available']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for book in self.books.values():
                writer.writerow(book.to_dict())

    def load_books(self):
        try:
            with open('Books.csv', 'r', newline= "", encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.books = {}
                for row in reader:
                    book = Book.from_dict(row)
                    self.books[book.book_id] = book
                if self.books:
                    self.nxt_book_id = max(self.books.keys()) + 1
                else:
                    self.nxt_book_id = 101

            print("Books loaded successfully.")
            return True

        except FileNotFoundError:
            print('File Not Found')
            return False

    
    def save_members(self):

        with open('members.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['member_id','name', 'borrowed_books']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for member in self.members.values():
                writer.writerow(member.to_dict())

    def load_members(self):
        try:
            with open('members.csv', 'r', newline= "", encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.members = {}
                for row in reader:
                    member = Member.from_dict(row)
                    self.members[member.member_id] = member

                if self.members:
                    self.nxt_member_id = max(self.members.keys()) + 1
                else:
                    self.nxt_member_id = 1

            print("Members loaded successfully.")
            return True

        except FileNotFoundError:
            print('File Not Found')
            return False

    def view_books(self):
        if not self.books:
            print("No books available.")
            return False
        print(f"{'Book Id':<10}{'Title':<15}{'Author':<15}{'Available'}")
        print('-'*45)
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(f"{book.book_id :<10}{book.title:<15}{book.author:<15}{status}")
        return True

    def view_members(self):
        if not self.members:
            print("No members Registered.")
            return False
        print(f"{'Member Id':<10}{'Name':<15}{'Books Borrowed'}")
        print('-'*40)
        for member in self.members.values():
            books = ", ".join(map(str, member.borrowed_books))
            if not books:
                books = "-"
            print(f"{member.member_id :<10}{member.name:<15}{books}")
        return True
