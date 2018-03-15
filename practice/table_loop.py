def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def table_title():
    print("months\ta\tb\tc")


def summary(months):
    print("Cages will run out in month", months)


a = 0
b = 1
c = a + b
month = 0
if a == 0:
    table_title()
    month += 1
    a = b

else:
    while c <= 500:
        c = fib(a)
        b = c - a
        print(month, "\t\t", a, "\t", b, "\t", c)
        month += 1
        a = c

summary(month)

