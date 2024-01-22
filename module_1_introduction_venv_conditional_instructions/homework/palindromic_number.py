def is_palindrome(str_number: str):
    # Compare the string with its reversed version
    if str_number == str_number[::-1]:
        return print("The number is palindrome")
    else:
        return print("The number is not palindrome")


number = input("Give me a number: ")
is_palindrome(number)