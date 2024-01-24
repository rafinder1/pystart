# Receive a number from the user and then display it
# this number raised to the power of 2, 3, 4 and 5.
# Use a for loop!

number = int(input("Give me a number: "))

result = 1
for i in [2, 3, 4, 5]:
    for j in range(0, i):
        result *= number
    print(result)
    result = 1
