seconds = float(input("How many seconds? "))

hours = seconds // 3600

minutes = seconds % 3600 / 60

print(f"{hours:02.0f}:{minutes:02.0f}")
