seconds = float(input("How many seconds? "))

hours = seconds / 60 / 60

minutes = hours % 1 * 60

print(f"{int(hours)}:{int(minutes)}")
