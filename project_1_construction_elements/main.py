walls = int(input("How many walls do you have to painting? "))

print("If you want assign previously height wall, you press enter")

for i in range(1, walls + 1, 1):
    width_wall = float(input(f"Give me a width {i} wall: "))
    height_wall = float(input(f"Give me a height {i} wall: "))
    print(i)
