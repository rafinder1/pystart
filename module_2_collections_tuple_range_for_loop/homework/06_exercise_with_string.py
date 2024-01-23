text = input("Give me text: ")

print(text[::-1])

text = text.replace(" ", "")
text = text.replace("!", "")
text = text.replace("?", "")

print(f"Text without spaces and punctuation {text}")
