import math
"""
Robert Matthews
CS 1400
Section 002
Exercise 3

3.1
Chapter 3, Discussion #2, pg. 78. Translate each of the expressions given in the problem into Python code. Execute each
expression in the shell, using reasonable input values where necessary. Make a session record of your interactions with
the shell (save the interaction to a file) and submit it as your answer.
"""

"""
Translate each of the following mathematical expressions into an equivalent Python expression. You may assume that the 
math library has been imported (via import math).
"""

print("This program will calculate all 5 expressions from Chapter 3, Discussion 2")
print("User input will be required for expression b, c, d, and e")


# a) (3 + 4)(5)
def calculate_expression_a():
    return (3 + 4) * 5


expression_a = calculate_expression_a()
print("expression a:", expression_a)


# b) (n(n - 1))/2
def calculate_expression_b(n):
    step_one = n * (n - 1)
    result = step_one / 2
    return result


variable_b1 = eval(input("Enter the value for the variable n in expression b: "))
expression_b1 = calculate_expression_b(variable_b1)
print("expression b:", expression_b1)


# c) 4*pi*r^2
def calculate_expression_c(r):
    step_one = r ** 2
    result = step_one * math.pi * 4
    return result


c1 = eval(input("Enter the value for the radius in expression c: "))
expression_c = calculate_expression_c(c1)
print("expression c:", expression_c)


# d) (y(cos a)^2 + y(sin b)^2)^(1/2)
def calculate_expression_d(a, b, y):
    first_half = y * (math.cos(a) ** 2)
    second_half = y * (math.sin(b) ** 2)
    result = math.sqrt(first_half + second_half)
    return result


d1 = eval(input("Enter the first variable in expression d: "))
d2 = eval(input("Enter the second variable assigned to the cos function in expression d: "))
d3 = eval(input("Enter the third variable assigned to the sin function in expression d: "))
expression_d = calculate_expression_d(d2, d3, d1)
print("expression d:", expression_d)


# e) (y2 - y1)/(x2 - x1)
def calculate_expression_e(x1, x2, y1, y2):
    first_half = y2 - y1
    second_half = x2 - x1
    result = first_half / second_half
    return result


e1 = eval(input("Enter the value for the first x coordinate in expression e: "))
e2 = eval(input("Enter the value for the second x coordinate in expression e: "))
e3 = eval(input("Enter the value for the first y coordinate in expression e: "))
e4 = eval(input("Enter the value for the second y coordinate in expression e: "))
expression_e = calculate_expression_e(e1, e2, e3, e4)

print("expression E:", expression_e)
