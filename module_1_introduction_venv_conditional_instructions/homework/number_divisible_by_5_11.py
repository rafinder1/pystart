number = float(input("Give me number: "))

rest_from_division_by_5 = number % 5
rest_from_division_by_11 = number % 11

if number == 0:
    print("Number is not divisible by 5 and 11 ")
elif rest_from_division_by_11 == 0 and rest_from_division_by_5 == 0:
    print("Number divisible by 5 and 11")
elif rest_from_division_by_5 == 0:
    print("Number divisible by 5 ")
elif rest_from_division_by_11 == 0:
    print("Number divisible by 11 ")
else:
    print("Number is not divisible by 5 and 11 ")