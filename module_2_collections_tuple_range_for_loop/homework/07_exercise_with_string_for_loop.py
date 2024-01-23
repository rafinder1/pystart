test = "Ala ma kota XD XD LOL"

print("Ex. 3")
for index, word in enumerate(test.split(" ")):
    if (index + 1) % 2 == 0:
        print(word.lower())
    else:
        print(word.upper())

print("Ex. 4")
for word in test.split(" "):

    if word[0].lower() == word[-1].lower():
        print(word)

vowels = 'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y'
print("Ex. 5")
for word in test.split(" "):
    for vowel in vowels:
        word = word.lower().replace(vowel, "")
    print(word)
