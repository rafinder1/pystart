print("Welcome in calculator!")
print("In this calculator you can: addition (+), subtraction (-), division (/) "
      "and multiplication (*)")

operation = input("Decide operation (use above symbols): ")

if operation not in ['+', '-', '/', '*']:
    print("Wrong operations")
    quit()

print("Give me two numbers:")
number_one = float(input("Number one is: "))
number_two = float(input("Number two is: "))

match operation:
    case '+':
        result = number_one + number_two
    case '-':
        result = number_one - number_two
    case '/':
        result = number_one / number_two
    case '*':
        result = number_one * number_two
    case _:
        quit()

print(f"Your results is: {result}")
