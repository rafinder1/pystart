sentence = "raz raz dwa trzy"

word_counts = {}

words = sentence.split()
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)