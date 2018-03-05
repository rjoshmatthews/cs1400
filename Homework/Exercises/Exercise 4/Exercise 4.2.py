from graphics import *
"""
Robert Matthews
CS 1400
Section 002
Exercise 3

4.2
Chapter 4, Programming Exercises #2, pg. 126. Write a program to draw the target as specified. Submit the source code as
your answer. Do not submit a screen shot.

From the textbook:
An archer target consists of a central circle of yellow surrounded by concentric rings of blue, black, and white. Each 
ring has the same width, which is the same as the radius of the yellow circle. Write a program that draws such a target.
Hint: Objects drawn later will appear on top of objects drawn earlier.
"""


def main():

    # set window name, width, and height
    screen = GraphWin("Archery Target", 500, 500)
    center = Point(250, 250)

    # set radius to be referenced by each circle
    radius = 50

    # outer circles need drawn first and then colored in
    circle4 = Circle(center, radius * 4)
    circle4.setFill("white")
    circle3 = Circle(center, radius * 3)
    circle3.setFill("black")
    circle2 = Circle(center, radius * 2)
    circle2.setFill("blue")
    circle1 = Circle(center, radius * 1)
    circle1.setFill("yellow")
    circle4.draw(screen)
    circle3.draw(screen)
    circle2.draw(screen)
    circle1.draw(screen)

    screen.getMouse()
    screen.close()

main()
