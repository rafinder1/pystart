numbers = []

for _ in range(1, 6):
    numbers.append(int(input("Give me a number: ")))

print(f"Your numbers is: {numbers}")
print(f"Your max number is: {max(numbers)}")
print(f"Your min number is: {min(numbers)}")