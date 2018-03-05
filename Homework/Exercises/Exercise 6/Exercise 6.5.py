import math
"""
Robert Matthews
CS 1400
Section 002
Exercise 6

5. Chapter 6, Programming Exercises #3, pg 206. Write the indicated functions, solve the problem and submit your source
code as your answer.
"""

# surface area of a sphere is 4pir^2
radius = 10


def sphere_area(a_radius):
    area = 4 * math.pi * a_radius**2
    return area


print("{0:.2f}".format(sphere_area(radius)))


# volume of a sphere is 4/3πr^3
def sphere_volume(a_radius):
    volume = 4 / 3 * (math.pi * a_radius**3)
    return volume


print("{0:.2f}".format(sphere_volume(radius)))
