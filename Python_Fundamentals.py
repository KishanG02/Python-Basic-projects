# Level 1: Python Fundamentals (1–10)

# 1. Even or Odd
# Given an integer, determine whether it is even or odd.

# 2. Positive, Negative, or Zero
# Determine if a number is positive, negative, or zero.

# 3. Find the Largest of Three Numbers
# Input three numbers and print the largest.

# 4. Sum of First N Numbers
# Calculate the sum from 1 to N.

# 5. Multiplication Table
# Print the multiplication table of a given number up to 10.

# 6. Count Digits
# Count the number of digits in an integer.

# 7. Reverse a Number
# Reverse the digits of a number.

# 8. Check Leap Year
# Determine whether a year is a leap year.

# 9. Calculate Factorial
# Find factorial of a number using loops.

# 10. Swap Two Numbers
# Swap two variables without using a third variable.

import random

def evenorodd(num):
    if num%2==0:
        print(f"{num} is Even.\n")
    else:
        print(f"{num} is Odd.\n")

def pos_neg_zero(num):
    if num < 0:
        print(f"{num} is negative.\n")
    elif num > 0:
        print(f"{num} is positive.\n")
    else:
        print("Zero.\n")

def largest_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the largest.\n")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the largest.\n")
    elif num3 > num1 and num3 > num2:
        print(f"{num3} is the largest.\n")

def sum_of_n(num):
    sum = 0
    for i in range(num+1):
        sum += i
    print(f"{sum} is th sum upto {num} \n")

def mul_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    print(" ")

def count_digit(num):
    print(len(str(num)),"\n")

def reverse(num):
    print(num, str(num)[::-1], "\n")

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year.\n")
    elif year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year.\n")
    else:
        print(f"{year} is not a leap year.\n")

def fac(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact,"\n")

def swap(num1, num2):
    num1, num2 = num2, num1
    print(f"{num1}, {num2}, \n")

if __name__ == '__main__':
    
    var1 = random.randint(-100,100)
    var2 = random.randint(-100,100)
    var3 = random.randint(-100,100)
    var4 = random.randint(1000,3000)
    num = random.randint(1,20)

    print(var1, var2, var3, var4, num, "\n")

    evenorodd(var1)
    pos_neg_zero(var1)
    largest_of_three(var1,var2,var3)
    sum_of_n(var1)
    mul_table(var1)
    count_digit(var1*var2*var3)
    reverse(var1*var2*var3)
    leap_year(var4)
    fac(num)
    swap(var1,var3)