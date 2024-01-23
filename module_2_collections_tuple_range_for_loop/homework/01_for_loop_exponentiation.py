number = int(input("Give me a number: "))

exponentiation = 1
for i in [2, 3, 4, 5]:
    for j in range(0, i):
        exponentiation *= number
    print(exponentiation)
    exponentiation = 1
