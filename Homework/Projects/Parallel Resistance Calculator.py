r1 = eval(input("Enter r1: "))
r2 = eval(input("Enter r2: "))
# r3 = eval(input("Enter r3: "))
# r4 = eval(input("Enter r4: "))

step_one = 1 / r1
step_two = 1 / r2
# step_three = 1 / r3
# step_four = 1 / r4

rtotal = 1 / (step_one + step_two)
# rtotal = 1 / (step_one + step_two + step_three)
# rtotal = 1 / (step_one + step_two + step_three + step_four)

print("The total resistance for the parallel circuit is", rtotal, "ohms")
