print("Calculator area of triangle. Tell me coordinates: ")
x1 = float(input("x1 = "))
y1 = float(input("y2 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

area = 1 / 2 * abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1))

print(f"Area of triangle is equal = {area}")
