from library import Library

menu = """
=========================================
        📚 Library Management System
=========================================

1. Add Book
2. View All Books
3. Search Book
4. Remove Book

-----------------------------------------

5. Register Member
6. View All Members

-----------------------------------------

7. Borrow Book
8. Return Book

-----------------------------------------

9. Save Data
10. Load Data

-----------------------------------------

11. Exit

=========================================
"""



if __name__ == '__main__':


    library = Library()
    while True:
        print(menu)
        try:
            user_input = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid choice")
            continue
        else:
            match user_input:
                    case 1:
                        print('========== Add Book ==========')
                        title = input("Enter Book Title : ")
                        author = input("Enter Author Name :")
                        if not title or not author:
                            print("Title and Author are required")
                            continue
                        else:
                            library.add_book(title,author)
                    case 2:
                        print('========== View All Books ==========')
                        library.view_books()

                    case 3:
                        print('========== Search Book ==========')
                        book_id = int(input("Enter Book ID : "))
                        if not book_id:
                            print("Book ID is required")
                            continue
                        else:
                            library.search_book(book_id)
                    case 4:
                        print('========== Remove Book ==========')
                        book_id = int(input("Enter Book ID : "))
                        if not book_id:
                            print("Book ID is required")
                            continue
                        else:
                            library.remove_book(book_id)
                    case 5:
                        print('========== Register Member ==========')
                        name = input("Enter Member Name : ")
                        if not name:
                            print("Member Name is required")
                            continue
                        else:
                            library.register_member(name)
                    case 6:
                        print('========== View All Members ==========')
                        library.view_members()
                    case 7:
                        print('========== Borrow Book ==========')
                        member_id = int(input("Enter Member ID : "))
                        book_id = int(input("Enter Book ID : "))
                        if not member_id or not book_id:
                            print("Member ID and Book ID are required")
                            continue
                        else:
                            library.borrow_book(member_id, book_id)
                    case 8:
                        print('========== Return Book ==========')
                        member_id = int(input("Enter Member ID : "))
                        book_id = int(input("Enter Book ID : "))    
                        if not member_id or not book_id:
                            print("Member ID and Book ID are required")
                            continue
                        else:
                            library.return_book(member_id, book_id)
                    case 9:
                        print('========== Save Data ==========')
                        library.save_books()
                        library.save_members()
                    case 10:
                        print('========== Load Data ==========')
                        library.load_books()
                        library.load_members()
                    case 11:
                        library.save_books()
                        library.save_members()
                        print('========== Exit ==========')
                        break
                    case _:
                        print("Invalid choice")
                        continue