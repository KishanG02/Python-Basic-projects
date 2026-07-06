import json

def display_menu():
    menu = """
    =====================
        Contact Book
    =====================
    1. Add Contact
    2. View Contacts
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Save Contacts
    7. Load Contacts
    8. Exit
    """
    print(menu)

def add_contact(contact_book):
    name = input("Enter name: ").strip()
    if name in contact_book:
        print("Contact already exists.")
    else:
        phone = input("Enter the number: ").strip()
        if len(phone) != 10 or not phone.isdigit():
            print("Enter valid number.")
        else:
            email = input("Enter the mail: ").strip()
            if "@" not in email or "." not in email:
                print("Email is not valid.")
            else:
                contact_book[name] = {
                    "phone": phone,
                    "email": email,
                }
                print(f"{name} is added to the contacts.\n")

def view_contacts(contact_book):
    if len(contact_book) != 0:
        print(f"{'Name':<15}{'Phone no':<15}{'Email'}")
        print("-"*45)
        for name,details in contact_book.items():
            print(f"{name:<15}{details['phone']:<15}{details['email']}")
    else:
        print("No Contacts Available.")

def search_contact(contact_book):
    name =  input("Enter contact name: ").strip()
    if name in contact_book:
        print(f"Name: {name}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}")
    else:
        print("Contact Not found.")

def update_contact(contact_book):
    name = input("Enter name: ")
    if name in contact_book:
        print(f"Current details\n {'-'*10}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}")
        phone = input("Enter the updated number: ").strip()
        if not phone:
            pass
        elif len(phone)!=10 or not phone.isdigit():
            print("Enter a valid number")
        else:
            contact_book[name]['phone'] = phone

        email = input("Enter the updated mail: ").strip()
        if not email:
            pass
        elif "@" not in email or "." not in email:
            print("Email is not Valid.")
        else:
            contact_book[name]['email'] = email
        print(f"{name} information is updated.")
    else:
        print("Contact Not Exists.")

def delete_contact(contact_book):
    name = input("Enter the name: ").strip()
    if name in contact_book:
        user_confirmation = input("Are you sure?(y/n): ").strip().lower()
        if user_confirmation.startswith("y"):
            del contact_book[name]
            print(f"{name} is deleted from the contacts.")
        else:
            print("Deletion Cancelled")
    else:
        print("Contact Not Found.")

def save_contacts(contact_book):
    with open("contacts.json", "w", encoding= "utf-8")as f:
        json.dump(contact_book,f, indent= 4)
    print("Contacts saved successfully.")

def load_contacts():
    try: 
        with open("contacts.json", "r", encoding= "utf-8") as f:
            contacts = json.load(f)
        print("Contacts loaded successfully.")
        return contacts
    except FileNotFoundError:
        print("No saved contact found.")
        return {}

if __name__ == "__main__":

    operation = {
        1: add_contact,
        2: view_contacts,
        3: search_contact,
        4: update_contact,
        5: delete_contact,
        6: save_contacts
    }

    contact_book = load_contacts()
    
    while True:
        display_menu()
        user_input = int(input("Enter the choice: "))
        if user_input in [1,2,3,4,5,6]:
            operation[user_input](contact_book)
        elif user_input == 7:
            contact_book = load_contacts()
        elif user_input == 8:
            save_contacts(contact_book)
            print("bye")
            break
        else:
            print("Enter a valid choice: ")
