sentence = "Ala has a cat, cat has Ala"

word_count = len(sentence.split())

print("Number of words:", word_count)

letter_count = sum(c.isalpha() for c in sentence)
print("Number of letters:", letter_count)