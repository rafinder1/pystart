test = "Ala ma kota XD XD LOL"

print("Ex. 3")
# Receive a sentence from the user and then write it in such a way that individual words are written
# once in LOWER CAPS and once in CAPITAL letters.
sentence_ex_3 = ''
for index, word in enumerate(test.split(" ")):
    new_word = word.upper()
    if index % 2 == 0:
        new_word = word.lower()

    sentence_ex_3 = f'{sentence_ex_3} {new_word}'
print(sentence_ex_3)

print("Ex. 4")
# Below, write in lower case only those words from the given sentence that start and end
# with the same letter.
for word in test.split(" "):

    if word[0].lower() == word[-1].lower():
        print(word)


print("Ex. 5")
# Below, display all the words in the sentence with the vowels removed.
vowels = 'aeiouy'
sentence_ex_5 = ''
for char in test:
    if char.lower() not in vowels:
        sentence_ex_5 += char

print(sentence_ex_5)

