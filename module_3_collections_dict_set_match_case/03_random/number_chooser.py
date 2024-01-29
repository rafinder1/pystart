import math
import random

number = random.randint(1, 100)

number_pow = math.pow(number, 2)
number_sqrt = math.sqrt(number)

number_floor = math.floor(number_sqrt)
number_ceil = math.ceil(number_sqrt)

print(f"Your number is {number}")
print("Exp: ", number_pow, "Sqrt: ", number_sqrt)
print("Floor: ", number_floor, "Ceil: ", number_ceil)
