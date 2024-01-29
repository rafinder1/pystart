import random
from itertools import product

value_kart = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbol_kart = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = list(product(value_kart, symbol_kart))

print(random.choice(deck))