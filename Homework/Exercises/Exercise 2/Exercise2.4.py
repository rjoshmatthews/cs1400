# Robert Matthews
# CS 1400
# Section ??
# Exercise 2

"""4. Chapter 2, Programming Exercises #5, pg. 54.Modify the convert.py program so that it computes and prints a table
    of Celsius temperatures and Fahrenheit equivalents every 10 degrees from 0 - 100 degress C. Submit your
    source code as the answer. Do not submit results. """

# Below I've copied the convert.py code right out the textbook. I'll reference that in the new program
"""
# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The tempereature is", fahrenheit, "degrees Fahrenheit.")

main()
"""

def main():
    print("This program calculates a range of temperatures from Celsius and converts them into Fahrenheit")
    print()

    print("Celsius ","Fahrenheit")

    for celsiusRange in range(10):
        celsius = (celsiusRange * 10)
        fahrenheit = (9 / 5) * celsius + 32
        print(celsius, '\t\t', fahrenheit)

    # I reformatted the last line because the extra digit in 100 was causing 212 under fahrenheit to tab too far over
    """celsius100 = 100
    fahrenheit100 = (9 / 5) * celsius100 + 32
    print(celsius100, '\t', fahrenheit100)"""

main()