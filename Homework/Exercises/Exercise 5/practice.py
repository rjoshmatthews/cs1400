# from graphics import *
import graphics
v1 = 4 - 3 / 2 + 1
print(v1)


# p1 = Point(5,1)
p1 = graphics.Point(5,1)

a = 7.0 / 2.0

print(a)

max = 25
part = 7
rem = max % part

print(rem)

userinput = eval(input("Enter the amount of feet you would like to convert to feet + inches: "))

divisor = 1

feet = userinput // divisor
inches_calc = userinput % divisor
inches = "{0:.2f}".format(inches_calc * 12)
print(userinput, "calculates to", feet, "ft and", inches, "in.")
