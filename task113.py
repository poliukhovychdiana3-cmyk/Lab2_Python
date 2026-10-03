a = int(input())
b = int(input())

product = a * b
summa = a + b

if product > summa:
    print(product)
elif product < summa:
    print(summa)
else:
    print(a - b)