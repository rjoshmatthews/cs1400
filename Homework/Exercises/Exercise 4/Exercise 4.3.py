from graphics import *
import math
"""
Robert Matthews
CS 1400
Section 002
Exercise 3

4.3
Suppose two circles are on the screen. Write a program that will do the following:
a) take as user input from the console the center point and radius for two circles
b) draw them in a window

c) write an expression in a comment to determine if the two circles overlap (hint: what's true if they overlap?)
"""

# set window
screen = GraphWin("Circles Test", 500, 500)
text_location = Point(250, 490)

# create input for circle centers and radii
print("Please click in the window to place the center of circle one: ")
instruction1 = Text(text_location, "Please click to place the center of circle one: ")
instruction1.draw(screen)
point1 = screen.getMouse()
radius1 = eval(input("Please enter the radius of circle one: "))
instruction1.undraw()
print()

print("Please click in the window to place the center of circle two: ")
instruction2 = Text(text_location, "Please click to place the center of circle two: ")
instruction2.draw(screen)
point2 = screen.getMouse()
radius2 = eval(input("Please enter the radius of circle two: "))
instruction2.undraw()
print()

# draw circle 2
circle1 = Circle(point1, radius1)
circle1.draw(screen)

# draw circle 2
circle2 = Circle(point2, radius2)
circle2.draw(screen)

# use formula to calculate if circle overlap

# pythagorean theorem will be used. Solving for C will require A^2 + B^2 = C^2
# A = (x-coordinate of center 2) - (x-coordinate of center 1)
# B = (y-coordinate of center 2) - (y-coordinate of center 1)

# If radius 1 + radius 2 is greater than C, the circles will overlap
# Radius 1 is called radius1, " " " " is called radius2, and C is called result

"""
def calculate_distance(point1, point2):
    part_one = point2.getX() - point1.getX()
    part_two = point2.getY() - point1.getY()
    part_three = (part_one ** 2) + (part_two ** 2)
    result = math.sqrt(part_three)
    return result

distance = calculate_distance(point1, point2)
overlap = radius1 + radius2
if distance > overlap
return true
else false
"""

# hold circles until user gives input to close window
instruction3 = Text(text_location, "Please click anywhere to quit: ")
instruction3.draw(screen)
screen.getMouse()
screen.close()
