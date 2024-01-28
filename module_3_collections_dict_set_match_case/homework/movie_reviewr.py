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

new_movies = []
for movie in movies:
    if movie['director'] != 'Steven Spielberg':
        new_movies.append(movie)
print(movies)
