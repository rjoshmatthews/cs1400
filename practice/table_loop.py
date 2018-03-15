def line_print(x, months):
    y = x - 1
    z = y + x
    print(months, "\t\t", x, "\t", y, "\t", z)
    x = y + x
    months += 1
    return x, months


def table_title():
    print("months\ta\tb\tc")


def summary(months):
    print("Cages will run out in month", months)


while True:
    a = 0
    b = 1
    c = a + b
    month = 0
    if month == 0:
        table_title()
        a = c
        month += 1

    else:
        while c >= 500:
            line_print(a, month)
            a = c
            month += 1

        summary(month)
