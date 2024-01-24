text = input("Give me text: ")

# Write a program that will take any string of characters from the user and print it on the screen
# in reverse order.
print(text[::-1])

# Write a program that will take a string of characters from the user and return the same text
# without spaces and punctuation.
sentence = ''
for char in text:
    if char.isnumeric() or char.isalpha():
        sentence += char
print(f"Text without spaces and punctuation {sentence}")
