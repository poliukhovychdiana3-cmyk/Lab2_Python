day = int(input())
month = int(input())
year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    leap = True
else:
    leap = False

if month == 2:
    if leap:
        days = 29
    else:
        days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 31

day = day + 1

if day > days:
    day = 1
    month = month + 1

    if month > 12:
        month = 1
        year = year + 1

print(str(day) + "." + str(month) + "." + str(year))