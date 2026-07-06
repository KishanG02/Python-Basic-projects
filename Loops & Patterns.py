# Level 2: Loops & Patterns (11 - 20)

# 11. Print Fibonacci Series
# Print first N Fibonacci numbers.

# 12. Find Sum of Digits
# Calculate sum of digits of a number.

# 13. Armstrong Number
# Check whether a number is Armstrong.

# 14. Palindrome Number
# Check if a number is palindrome.

# 15. Prime Number Check
# Determine if a number is prime.

# 16. Print All Prime Numbers Between 1 and N

# 17. Count Prime Numbers in a Range

# 18. Star Pattern Pyramid
# Example:
#
#   *
#  ***
# *****

# 19. Inverted Pyramid Pattern

# 20. Floyd's Triangle
# Example:

# 1
# 2 3
# 4 5 6
# 7 8 9 10

import random
from math import sqrt

def fibonacci(n):
    a, b =0, 1
    print(a)
    for i in range(n):
        print(b)
        a, b = b, a+b
    print("")
        

def sum_of_digits(n):
    sum = 0
    for char in str(n):
        sum += int(char)
    print(f"{n}'s sum is {sum}.\n") 
        
def armstrong(n):
    length = len(str(n))
    sum = 0
    for i in range(length):
        sum += int(str(n)[i])**length
    if sum == n:
        print(f"{n} is a armstrong number.\n")
    else:
        print(f"{n} is not armstrong number.\n")

def palindrome(n):
    num = ""
    for i in range(len(str(n))-1,-1,-1):
        num += str(n)[i]
    
    if n == int(num):
        print(f"{n} is a palindrome.\n")
    else:
        print(f"{n} is not a palindrome.\n")

def prime(n):
    for i in range(2,int(sqrt(n))):
        if n % i == 0:
            return f"{n} is not prime.\n"
            break
    return f"{n} is prime.\n"

def prime_num(n):
    
    prime = []

    for num in range(2, n+1):
        is_prime = True
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
                prime.append(num)
    print(prime, "\n")

def count_prime_num(n):
    
    prime = []

    for num in range(2, n+1):
        is_prime = True
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
                prime.append(num)
    print(len(prime), "\n")

def pyramid(n):
    for i in range(n):
        for j in range(1,n-i):
            print(end = "  ")
        for j in range((i*2)+1):
            print("*", end = " ")
        print(" ")
    print("\n")

def inverted_pyd(n):
    for i in range(n-1, -1, -1):
        for j in range((i*2)+1):
            print("*", end = " ")
        print(" ")
        for j in range(n-i, 0, -1):
            print(end = "  ")
    print("\n")

def floyd(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end="")
            num += 1
        print(" ")
        
if __name__ == '__main__':

    var1 = random.randint(0,10)
    var2 = random.randint(10000,1000000)
    var3 = random.randint(10, 100000)
    var4 = random.randint(1,20)

    print(var1, var2, var3, var4, "\n")

    fibonacci(var1)
    sum_of_digits(var2)
    armstrong(var3)
    palindrome(var4)
    print(prime(var4))
    prime_num(var4)
    count_prime_num(var4)
    pyramid(var1)
    inverted_pyd(var1)
    floyd(var1)