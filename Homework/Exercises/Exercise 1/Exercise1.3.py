# Robert Matthews
# CS 1400
# Section ??
# Exercise 1

# 1.3
# File: chaos.py
# A simple program illustrating chaotic behavior.


def chaos():

    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))

    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


chaos()
