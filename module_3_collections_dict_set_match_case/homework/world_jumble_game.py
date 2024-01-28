import random

list_words = ['python', 'fix', 'merge', 'commit', 'add']

word = random.choice(list_words)
lista_letters = list(word)

random.shuffle(lista_letters)

shuffled_word = ''.join(lista_letters)
print("Word to guess: ", shuffled_word)

for i in range(3):
    user_word = input("What word is that? ")

    if word == user_word:
        print("You Win!")
        quit()
    else:
        print("Try again.")

print("You Lose")