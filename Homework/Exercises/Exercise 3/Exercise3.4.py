"""
Robert Matthews
CS 1400
Section 002
Exercise 3

3.4
Chapter 3, Programming Exercises #2, pg. 79. Write a program to calculate the cost/sq. inch of a circular pizza given
the diameter and total price. Submit the code as your answer. Do not submit results.
"""


def main():
    import math
    pizzaCostRaw = eval(input("Enter the cost of the pizza: "))
    pizzaDiameter = eval(input("Enter the diameter in inches of the pizza: "))
    print()

    pizzaCostFormat = "${0:.2f}".format(pizzaCostRaw)
    pizzaSqrIn = math.pi * (pizzaDiameter/2)**2
    sqrInCost = pizzaCostRaw / pizzaSqrIn

    print("Your", pizzaDiameter,"inch pizza cost", pizzaCostFormat)
    print("The price per square inch for your pizza is", "${0:.2f}".format(sqrInCost))


main()

