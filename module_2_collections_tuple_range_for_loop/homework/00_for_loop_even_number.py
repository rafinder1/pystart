number = int(input("Give me a number: "))

sum_numbers = 0
for index, element in enumerate(range(2, number + 1, 2)):
    sum_numbers += element
    print(element, end=", ")

print("")
print(f"Sum numbers: {sum_numbers}")
count_numbers = index + 1

print(f"Count number: {count_numbers}")

print(f"Average numbers: {sum_numbers / count_numbers}")

print(f"Product of numbers: {sum_numbers * count_numbers}")
