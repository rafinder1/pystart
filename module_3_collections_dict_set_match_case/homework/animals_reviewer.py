animals = {
    'dog': 4,
    'cat': 4,
    'horse': 4,
    'millipede': 100
}
max_count_legs = 0
animal_most_legs = None
for animal, legs in animals.items():
    if legs > max_count_legs:
        animal_most_legs = animal

print(animal_most_legs)
