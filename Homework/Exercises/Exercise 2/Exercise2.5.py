
"""
Robert Matthews
CS 1400
Section ??
Exercise 2

5. Chapter 2, Programming Exercises #6, pg. 54.Modify the futval.py program as indicated in your text.
    Submit your source code as the answer. Do not submit results.
"""

# A program to compute the value of an investment carried into the future

def main():
    print("This program calculates the future value of a multi-year investment")
    print()

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    timeLength = eval(input("Enter the length of time in years: "))

    for i in range(timeLength):
        principal = principal * (1 + apr)

    print("The value in", timeLength, "years is:", "$" + "{0:.2f}".format(principal))

main()