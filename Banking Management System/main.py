from bank import Bank

def display_menu():
    menu = """
    =========================
    Banking System
    =========================

    1. Create Account
    2. Deposit Money
    3. Withdraw Money
    4. Check Balance
    5. Transfer Money
    6. Transaction History
    7. View All Accounts
    8. Save Accounts
    9. Load Accounts
    10. Exit
    """
    print(menu)


if __name__ == '__main__':

    obj = Bank()

    while True:

        display_menu()
        user_input = int(input("Enter a Choice: "))

        match user_input:
            case 1:
                name = input("Enter Name: ")
                obj.create_account(name)

            case 2 | 3:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount: "))
                if user_input == 2:
                    obj.deposit_money(amount, account_number)
                elif user_input == 3:
                    obj.withdraw_money(amount, account_number)

            case 4:
                account_number = int(input("Enter account number: "))
                print(obj.check_balance(account_number))
                
            case 5:
                from_account_number = int(input("Enter sender account number: "))
                to_account_number = int(input("Enter receiver account number: "))
                amount = float(input("Enter amount: "))
                obj.transfer_money(amount, from_account_number, to_account_number)

            case 6:
                account_number = int(input("Enter account number: "))
                print(obj.transaction_history1(account_number))

            case 7:
                obj.view_all()

            case 8:
                obj.save_accounts()

            case 9:
                obj.load_accounts()

            case 10:
                obj.save_accounts()
                print("Thankyou for using our Bank.")
                break