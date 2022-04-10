import random

with open("movies.txt") as file:
    movies = file.readlines()
    print(random.choice(movies))