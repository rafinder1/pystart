import random

dishes = {
    'soup': ['tomato', 'borscht', 'chicken broth'],
    'dinner': ['meatballs', 'schnitzel', 'doves'],
    'dessert': ['ice-cream', 'jelly', 'cake']
}

for dish, options in dishes.items():
    print(dish, '-', random.choice(options))
