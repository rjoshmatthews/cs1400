"""
Robert Matthews
CS 1400
Section 002
Exercise 7

7.1
Chapter 7, Discussion #3, pg. 237.
"""


# show output for silly structure that would result from the following inputs:
def silly(x, y, z):

    if x > y:
        if y > z:
            print("Spam Please!")
        else:
            print("It's a late parrot!")
    elif y > z:
        print("Cheese Shoppe")
        if x >= z:
            print("Cheddar")
        elif x < y:
            print("Gouda")
        elif z == y:
            print("Swiss")
    else:
        print("Trees")
        if x == y:
            print("Chestnut")
        else:
            print("Larch")
    print("Done")


def print_statement(letter, l, m, n):
    print(letter, ") = ")
    print(silly(l, m, n))
    print()


print_statement('a', 3, 4, 5)
print_statement('b', 3, 3, 3)
print_statement('c', 5, 4, 3)
print_statement('d', 3, 5, 2)
print_statement('e', 5, 4, 7)
print_statement('f', 3, 3, 2)
