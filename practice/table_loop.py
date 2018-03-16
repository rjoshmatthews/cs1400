def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def table_title():
    print("months\tparents\tbabies\ttotal")


def summary(months):
    print("Cages will run out in month", months)



table_title()

total = 2
parents = 2
month = 0
babies = 0
babies_per_parent = 2
cages = 500
parents_per_cage = 2

while int(total) < cages * parents_per_cage:
    month += 1
    # promote month old babies to parents.
    parents += babies

    # calculate new babies from parents
    babies = int(parents/2) * babies_per_parent
    total = parents + babies

    print(month, "\t\t", parents, "\t\t", babies, "\t\t", total)

summary(month)

