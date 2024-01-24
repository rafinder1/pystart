# Write a program that will receive an integer from the user,
# and then it will display all even numbers on the screen
# from 2 to this number. Display all these numbers separated by commas.

number = int(input("Give me a number: "))

sum_numbers = 0
for index, element in enumerate(range(2, number + 1, 2)):
    sum_numbers += element
    print(element, end=", ")

print("")

# Below, display the sum, number, average, and product of these numbers.

print(f"Sum numbers: {sum_numbers}")
count_numbers = index + 1

print(f"Count number: {count_numbers}")

print(f"Average numbers: {sum_numbers / count_numbers}")

print(f"Product of numbers: {sum_numbers * count_numbers}")
