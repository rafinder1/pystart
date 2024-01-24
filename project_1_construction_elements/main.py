import math

walls = int(input("How many walls do you have to painting? "))

print("If you want assign previously height wall, you press enter")
previous_height = 3
total_area = 0

for i in range(1, walls + 1, 1):
    width_wall = float(input(f"Give me a width {i} wall: "))
    height_wall = input(f"Give me a height {i} wall: ")

    if height_wall.isnumeric():
        height_wall = float(height_wall)
        previous_height = height_wall
    else:
        height_wall = previous_height

    total_area += width_wall * height_wall

print(f"Total area is equal: {total_area}")
layers_of_base = float(input("Tell me the number of layers of base: "))
layers_of_paint = float(input("Tell me the number of layers of paint: "))

liters_of_base = math.ceil(total_area * layers_of_base / 5)
liters_of_paint = math.ceil(total_area * layers_of_paint / 13)

print(f"You need base: {liters_of_base} l.")
print(f"You need paints: {liters_of_paint} l.")