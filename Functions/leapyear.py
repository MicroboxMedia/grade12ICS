def isLeapYear(y):
    return y % 100 == 0 and y % 400 == 0 if y % 4 == 0 or y % 400 == 0 else False


print(isLeapYear(1800))


