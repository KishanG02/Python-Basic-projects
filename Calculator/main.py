def display_menu():
    menu = """======== calculator ===========
    1. Addition
    2. Subtraction
    3. Multiply
    4. Divide
    5. Modulus
    6. Power
    7. Exit 
    8. View History
    """
    print(menu)

def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero.")
        return None
    return num1 / num2

def mod(num1, num2):
    return num1%num2

def power(num1,num2):
    return num1**num2

def get_number():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 =  float(input("Enter Second number: "))
            return num1,num2
        except ValueError:
                print("Please enter a number.\n")
                continue

def calculate(u_input):
    operation = {
        1: ("+",add),
        2: ("-",sub),
        3: ("*",multiply),
        4: ("/",divide),
        5: ("%",mod),
        6: ("^",power)
    }
    num1,num2 = get_number()
    symbol, func = operation[u_input]
    result = func(num1,num2)
    if result is not None:
        memory.append({"operation": symbol,
                        "num1": num1,
                        "num2": num2,
                        "result": round(result,2)})
        print(f'{num1} {symbol} {num2} = {round(result,2)}')



if __name__ == '__main__':
    
    memory = []

    while True:
        display_menu()

        try:
            u_input = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.\n")
            continue

        if u_input in [1,2,3,4,5,6]:
            calculate(u_input)
            
        elif u_input == 7:
            print("Thankyou for using the calculator.")
            break

        elif u_input == 8:
            print(memory)
        
        else:
            print("Invalid Choice.")