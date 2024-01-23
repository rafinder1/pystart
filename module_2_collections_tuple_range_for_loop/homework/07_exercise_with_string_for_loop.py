test = "Ala ma kota XD XD LOL"

print("Ex. 3")
# Receive a sentence from the user and then write it in such a way that individual words are written
# once in LOWER CAPS and once in CAPITAL letters.
for index, word in enumerate(test.split(" ")):
    if (index + 1) % 2 == 0:
        print(word.lower())
    else:
        print(word.upper())

print("Ex. 4")
# Below, write in lower case only those words from the given sentence that start and end
# with the same letter.
for word in test.split(" "):

    if word[0].lower() == word[-1].lower():
        print(word)

vowels = 'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y'
print("Ex. 5")
# Below, display all the words in the sentence with the vowels removed.
for word in test.split(" "):
    for vowel in vowels:
        word = word.lower().replace(vowel, "")
    print(word)
