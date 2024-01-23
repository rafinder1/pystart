# Ask the user for a number, and the result will display whether
# it is a prime number.
import math

number = int(input("Give me a number: "))

count = 0
for i in range(2, number + 1):
    if number % i == 0:
        count += 1

is_prime = True
for div in range(2, math.ceil(math.sqrt(number)) + 1):
    if number % div == 0:
        is_prime = False
        break

if count == 1:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")
