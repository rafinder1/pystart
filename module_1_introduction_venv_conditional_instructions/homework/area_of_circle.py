import math

print("Calculator area of circle. Tell me coordinates: ")
x1 = float(input("x1 = "))
y1 = float(input("y2 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

x = (x1 + x2) / 2
y = (y1 + y2) / 2
print(f"The center line is in: \n"
      f"x_center = {x:.2f} \n"
      f"y_center = {y:.2f}")

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
r = d / 2
print(f"Radios is equal: {r:.2f}")

area_circle = math.pi * r ** 2

print(f"Area of circle is equal: {area_circle:.2f}")

rectangle_a = math.sqrt((x1 - x2) ** 2 + (y2 - y2) ** 2)
rectangle_b = math.sqrt((x1 - x1) ** 2 + (y1 - y2) ** 2)

area_rectangle = rectangle_a * rectangle_b

print(f"Area of rectangle is equal: {area_rectangle:.2f}")
