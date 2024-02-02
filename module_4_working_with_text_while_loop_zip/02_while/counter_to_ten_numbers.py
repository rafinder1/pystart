numbers: list = []

while len(numbers) < 10:
    number = int(input("Give me a positive number: "))

    if number > -1:
        numbers.append(number)
    else:
        print("You must add positive number.")

print(f"Your numbers: {numbers}")
print(f"Length your numbers: {len(numbers)}")
