import math

side = float(input("What is the side of an equilateral triangle? "))

area_triangle = (side ** 2 * math.sqrt(3)) / 4

print(f"Area of triangle is equal {area_triangle:.2f}")