polish_english = {
    "do": "robić",
    "walk": "chodzić",
    "play": "grać"
}

word = input("Give me word Polish/English: ")

in_dictionary = False
for polish, english in polish_english.items():
    if word == polish:
        print(f"{word} in polish is: {english}")
        in_dictionary = True
        break
    elif word == english:
        print(f"{word} in english is: {polish}")
        in_dictionary = True
        break

if not in_dictionary:
    print("This word is not in the dictionary")