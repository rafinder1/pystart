numbers = tuple(range(12, 1025, 6))

print(f"Numbers is {len(numbers)}")

print(f"The first three numbers: {numbers[:3]}")

print(f"Penultimate item on the list: {numbers[-2]}")

print(f"Every sixth element starting from the fourth {numbers[4::6]}")

print(f"Every third element counting from the end {numbers[::-3]}")

print(f"average of the last 10 values: {sum(numbers[-10:]) / 10}")
