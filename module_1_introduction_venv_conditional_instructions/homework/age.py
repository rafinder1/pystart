from datetime import datetime

current_year = datetime.now().year

birth_year = float(input("What is your year of birth? "))

years_old = int(current_year - birth_year)

print(f"You have {years_old} years old.")

def is_leap_year(year):
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

is_leap_year(birth_year)