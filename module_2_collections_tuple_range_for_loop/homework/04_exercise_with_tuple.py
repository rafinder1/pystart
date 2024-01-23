# Create a tuple containing numbers divisible by 6 from 12 to 1024

numbers = tuple(range(12, 1025, 6))

# ➔ How many of these numbers are there?
print(f"Numbers is {len(numbers)}")

# ➔ Display the first three numbers
print(f"The first three numbers: {numbers[:3]}")

# ➔ Penultimate element
print(f"Penultimate item on the list: {numbers[-2]}")

# ➔ Every sixth element starting from the fourth
print(f"Every sixth element starting from the fourth {numbers[4::6]}")

# ➔ Every third element counting from the end
print(f"Every third element counting from the end {numbers[::-3]}")

# ➔ What is the average of the last 10 values?
print(f"average of the last 10 values: {sum(numbers[-10:]) / 10}")
