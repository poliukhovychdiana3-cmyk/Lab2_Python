room = input()

if room == "triangle":
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(area)

elif room == "rectangle":
    a = float(input())
    b = float(input())

    area = a * b
    print(area)

elif room == "circle":
    r = float(input())

    area = 3.14 * r ** 2
    print(area)