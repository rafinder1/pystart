movies = [
    {
        'title': 'The Lost World: Jurassic Park',
        'director': 'Steven Spielberg',
        'year_production': 1997
    },
    {
        'title': 'Fast and Furious 10',
        'director': 'Louis Leterrier',
        'year_production': 2023
    },
]

for index, movie in enumerate(movies):
    if movie['director'] == 'Steven Spielberg':
        movies.pop(index)
print(movies)
