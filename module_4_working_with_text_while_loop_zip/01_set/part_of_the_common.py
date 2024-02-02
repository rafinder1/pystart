numbers_divisible_by_3 = set(range(3, 101, 3))
numbers_divisible_by_5 = set(range(5, 101, 5))

numbers_divisible_by_3_and_5 = numbers_divisible_by_3 & numbers_divisible_by_5

print(f"Number divisible by 3 and 5: {numbers_divisible_by_3_and_5}")
