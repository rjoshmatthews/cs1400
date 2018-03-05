"""
Robert Matthews
CS 1400
Section ??
Exercise 2

Write a console application that helps a user calculate a range of tips and total cost for a meal. When the user enters
a value in dollars and cents, your program will calculate three possible tip amounts as described below.

For excellent service calculate a tip that is 20% of the cost of the meal.
For average service, calculate a tip that is 15% of the cost of the meal.
For poor service, calculate a tip that is 10% of the cost of the meal.
Display 4 lines on the screen:

the cost the user entered
each tip and total cost with that tip on separate line
Show all output as dollars and cents correct to 2 decimal places. Following is example
output of a program if the user enter 25.00 ($ is part of the prompt):
"""

# some easy solutions I found for this assignment was to assign the tip values as excellent, average, and poor. This
# helped me refer to them in the total (totalExcellent, etc etc). Another solution was to format the columns using "\t".
# That way all of the costs were aligned in the text when the print function ran.


def main():
# prompt to enter the cost of the meal
    mealCost = float(input("How much was your meal? "))

# calculate 3 possible tip amounts and the total cost with the tip
    tipExcellent = mealCost * 0.2
    tipAverage = mealCost * 0.15
    tipPoor = mealCost * 0.1

    totalExcellent = mealCost + tipExcellent
    totalAverage = mealCost + tipAverage
    totalPoor = mealCost + tipPoor

# display 4 lines on the screen
# line 1 = cost user entered
    print("The cost of the meal was","${0:.2f}".format(mealCost))
# line 2-4 each tip and total cost on separate lines
    print("For excellent service your tip will be","\t${0:.2f}".format(tipExcellent),
          "for a total cost of","${0:.2f}".format(totalExcellent))
    print("For average service your tip will be","\t${0:.2f}".format(tipAverage),
          "for a total cost of","${0:.2f}".format(totalAverage))
    print("For poor service your tip will be","\t\t${0:.2f}".format(tipPoor),
          "for a total cost of","${0:.2f}".format(totalPoor))

main()

# something I learned for this assignment was how to round off floats and display a currency. to find "${0:.2f}" I spent
# some time looking it up on google. It's a good resource!