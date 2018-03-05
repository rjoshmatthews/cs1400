"""
Robert Matthews
CS 1400
Section 002
Exercise 5

5.5
Chapter 5, Programming Exercise #6, pg. 172. Create the numerology program that counts full names, as indicated.
Assuming a name entered in is stored in a variable called name, what is the Pythonic way to read the third character
from the end?
"""

# I used the structure in the loop from Exercise 5.2 and used it to convert and add letters into the ord number
# starting with a-z. If you minus 96 from the ord number you get a == 1, b == 2, etc etc to z == 26

name = str(input("Enter the name you would like to calculate into a numeric value: "))
input_text = name.lower()


def letter_conversion(text):
    count = 0

    for letter in text:
        if not letter == ' ':
            count += ord(letter) - 96

    return count


numeric_name_value = letter_conversion(input_text)

print("The numeric value for the name is:", numeric_name_value)

# to read characters starting from the end you'll use a negative sign and the amount to count over inside of brackets.
# EX: input_text[-3]
