"""
Robert Matthews
CS 1400
Section 002
Exercise 5

5.3
Chapter 5, Discussion #1, pg. 169. Show the results of evaluating each of the string expressions listed for this
question in your text.
"""

s1 = "spam"
s2 = "ni!"

a = "The Knights who say, " + s2
b = 3 * s1 + 2 * s2
c = s1[1]
d = s1[1:3]
e = s1[2] + s2[:2]
f = s1 + s2[-1]
g = s1.upper()
h = s2.upper().ljust(4) * 3


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)