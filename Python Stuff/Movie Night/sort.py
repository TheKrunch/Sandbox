with open("movies.txt") as file:
    lines = file.readlines()
    lines.sort()

    with open("movies.txt", "w") as sorted:
        for line in lines:
            sorted.write(line)
    