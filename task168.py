n = int(input())

first = n // 100
second = (n // 10) % 10
last = n % 10

s = first + last

if s > second:
    print(">")
elif s < second:
    print("<")
else:
    print("=")