"""
Robert Matthews
CS 1400
Section 002
Exercise 8

8.4
Chapter 8, Programming Exercises #8, pg. 280
"""

# the greatest common divisor (GCD) of two values can be computed using Euclid's algorithm. starting with the values m
# and n, we repeatedly apply the formula: n, m = m, n % m until m is 0. At that point, n is the GCD of the original m
# and n. write a program that finds the GCD of two numbers using this algorithm.


# the easiest way to do this is to import the math module. Python 3.5's math library contains a function for greatest
# common divisor already. Below i've included my preferred method.

"""
import math

try:
    print("Please use only whole numbers")
    a = input("Please enter the first value: ")
    b = input("Please enter the second value: ")
    
    n = int(a)
    m = int(b)
    
    formula = math.gcd(n, m)
    print("The greatest common divisor of", a, "&", b, "is", formula)
    
except ValueError:
    if not input:
        print("User entered an empty value. Please try again.")
    else:
        print("User entered an incorrect value. PLease try again.")
"""


# below is the method I've created to apply the formula given from the textbook
def gcd(x, y):
    while y > 0:
        (x, y) = (y, x % y)
    return x


try:
    print("Please use only whole numbers")
    n = input("Please enter the first value: ")
    m = input("Please enter the second value: ")

    a = int(n)
    b = int(m)
    formula = gcd(a, b)
    print("The greatest common divisor of", n, "&", m, "is", formula)

except ValueError:
    if not input:
        print("User entered an empty value. Please try again.")
    else:
        print("User entered an incorrect value. Please try again.")

