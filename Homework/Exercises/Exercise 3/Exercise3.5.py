"""
Robert Matthews
CS 1400
Section 002
Exercise 3

3.5
Section 3.4, pg. 71 shows one way to write a factorial function, and it mentions that there are several other ways to do
 it. Modify the code to implement one of those ways. Submit your source code as the answer. Do not submit results.
"""

# from the book:
# factorial.py
#   Program to compute the factorial of a number
#   Illustrates for loop with an accumulator


# def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, n-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

# main()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("This program will calculate the factorial of any whole number")
factor = eval(input("Enter a number: "))
print(factorial(factor))
