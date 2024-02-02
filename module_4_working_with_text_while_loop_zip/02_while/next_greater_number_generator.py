import math
import statistics

numbers = []

last_number = -math.inf

while True:
    user_number = int(input("Give me a number: "))
    if user_number < last_number:
        break

    numbers.append(user_number)
    last_number = user_number

average = statistics.mean(numbers)

print(f"Your average from number is equal: {average}")
