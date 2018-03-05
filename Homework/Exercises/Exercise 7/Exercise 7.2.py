"""
Robert Matthews
CS 1400
Section 002
Exercise 7

7.2
Chapter 7, Programming Exercise #6, pg. 239. Submit your source code as your answer.
"""

# the speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the speed limit plus a penalty of
# $200 for any speed over 90 mph. write a program that acceps the speed limit and a clicked speed and either prints a
# message indicating the speed was legal or prints the amount of the fine, if the speed is illegal.

speed_limit = eval(input("Enter the speed limit: "))
speed = eval(input("Enter the clocked speed: "))
print()

high_fine = 200
fine = 50 + (5 * (speed - speed_limit))

if speed < speed_limit:
    print("You were driving safely!")
elif speed == speed_limit:
    print("You're starting to push the limits... Slow down!")

else:
    print("You were speeding! Tickets aren't cheap...")
    if speed >= 90:
        print("Your fine will be: ${0:.2f}".format(high_fine + fine))
    else:
        print("Your fine will be: ${0:.2f}".format(fine))

