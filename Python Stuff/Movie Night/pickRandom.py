import random
from time import sleep

with open("marieMovies.txt") as file:
    movies = file.readlines()
    print("Selecting a Random Movie from:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    for movie in movies:
        print(movie, end="")
        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print(random.choice(movies))