from graphics import *
import math
"""
Robert Matthews
CS 1400
Section 002
Project 3

Farmer John has four fields of soybeans planted. There are three months left until harvest time, and the almanac has
forecast a very dry summer. Farmer John has decided to put in a new, more efficient irrigation system to water his
soybean crops. His estimate is that the new system will cost about $10,000. Soybeans are going for about $9.86 a bushel,
so Farmer John wants to harvest as many bushels of soybeans as he possibly can. As he ponders on this problem, he
sketches a map of his soybean fields that shows how the irrigation system will cover the crops. This is shown in the
image above.

The square ABCD has it's vertices located at the centers of four identical circles, which are the regions covered by the 
new circular irrigation system. Farmer John is intrigued by the pattern shown in the shaded region of the map, and
wonders what the area of this shaded region is.

You have to solve two problems for this project:

Draw an image that looks like the image above on the screen. 
Compute the area of this shaded region, given the the length of one of the sides of the square--which can be a real
number--as user input. Your answer should be accurate to two decimal places.
User input may be console input, or may come from a text entry box in the GUI, or may come from mouse clicks in the 
window.
"""

try:
    print("NOTE: For user input, 50-300 is recommended. ")
    side_length = input("Please enter the side length of Farmer John's field: ")
    if int(side_length):
        # decide what kind of user input to use and then implement it as the radius
        radius = int(side_length) / 2

        # create window based off of input size (ensures that drawing will fit in window)
        screen = GraphWin("Farmer John's Field", radius * 6, radius * 6)

        # draw the square (use polygon function from graphics.py) and then fill it gray
        point1 = Point(radius * 2, radius * 2)
        point2 = Point(radius * 4, radius * 2)
        point3 = Point(radius * 4, radius * 4)
        point4 = Point(radius * 2, radius * 4)

        field = Polygon(point1, point2, point3, point4)
        field.draw(screen)
        field.setFill("gray")

        all_points = {point1, point2, point3, point4}

        # draw 4 circles above the square and color white
        circle_one = Circle(point1, radius)
        circle_two = Circle(point2, radius)
        circle_three = Circle(point3, radius)
        circle_four = Circle(point4, radius)

        circle_one.draw(screen)
        circle_two.draw(screen)
        circle_three.draw(screen)
        circle_four.draw(screen)

        circle_one.setFill("white")
        circle_two.setFill("white")
        circle_three.setFill("white")
        circle_four.setFill("white")
        # I wanted to create a loop to create, draw and shade all of the circles but ran out of time
        # did this one in a hurry

        # draw the same square again as an outline over the circles
        field_outline = Polygon(point1, point2, point3, point4)
        field_outline.draw(screen)

        # calculate non-shaded area in square
        def circle_area(a_radius):
            area = math.pi * a_radius ** 2
            return area


        def square_area(a_radius):
            side = a_radius * 2
            area = side * side
            return area


        def field_area(a_radius):
            area = square_area(a_radius) - circle_area(a_radius)
            return area


        print("The shaded area in Farmer John's field is",
              "{0:.2f}".format(field_area(radius)), "units squared"".")
        print("View window. Click anywhere in drawn window to close and end program. ")
        # waits until user input to close
        screen.getMouse()
        screen.close()
except ValueError:
    if not input:d
        print("User entered an empty value. Please try again.")
    else:
        print("User entered an incorrect value. PLease try again.")
