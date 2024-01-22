from datetime import datetime

current_year = datetime.now().year

birth_year = int(input("What is your year of birth? "))

age = int(current_year - birth_year)

print(f"You have {age} years old.")

if age >= 18:
    print("You are an adult")
else:
    print(f"You will be an adult in {18 - age} years.")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

is_leap_year(birth_year)