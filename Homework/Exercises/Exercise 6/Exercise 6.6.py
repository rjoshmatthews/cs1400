import math
from graphics import *
"""
Robert Matthews
CS 1400
Section 002
Exercise 6

6. Chapter 6, Programming Exercises #6, pg 207.  Write the function that computes the area of a triangle, as indicated.
Modify the triangle2.py code given in the chapter to use your function. Submit your source code as your answer.
"""


def square(a_side):
    return a_side ** 2


def distance_calc(p1, p2):
    distance = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return distance


def s_calc(a, b, c):
    s = (a + b + c) / 2
    return s


def triangle_area(a, b, c, s):
    area = math.sqrt(s * (s - a)*(s - b)*(s - c))
    return area


def main():
    screen = GraphWin("Triangle")
    screen.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(screen)

    # get and draw three vertices of a triangle
    p1 = screen.getMouse()
    p1.draw(screen)
    p2 = screen.getMouse()
    p2.draw(screen)
    p3 = screen.getMouse()
    p3.draw(screen)

    side_a = distance_calc(p1, p2)
    side_b = distance_calc(p2, p3)
    side_c = distance_calc(p3, p1)

    # use polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peach puff")
    triangle.draw(screen)

    # calculate the perimeter of the triangle
    # perimeter = side_a + side_b + side_c
    # message.setText("The perimeter is: {0:.2f}".format(perimeter))
    #
    # calculate the area of the triangle
    s = s_calc(side_a, side_b, side_c)
    area = triangle_area(side_a, side_b, side_c, s)
    message.setText("The area is: {0:.2f}".format(area))

    # wait for click to exit
    screen.getMouse()
    screen.close()


main()
