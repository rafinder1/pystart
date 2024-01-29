countries_cities = {
    'poland': 'warsaw',
    'germany': 'berlin',
    'france': 'paris'
}

points = 0

for country, city in countries_cities.items():
    capital = input(f"Capital of {country} is: ").lower()

    if capital == city:
        print("Correct")
        points += 1
print(f"You have {points} points")
