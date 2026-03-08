# Mini Project 1
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
# Mini Project 2
movies = [
("Eternal Sunshine of the Spotless Mind", 20000000),
("Memento", 9000000),
("Requiem for a Dream", 4500000),
("Pirates of the Caribbean: On Stranger Tides", 379000000),
("Avengers: Age of Ultron", 365000000),
("Avengers: Endgame", 356000000),
("Incredibles 2", 200000000)
]

n = int(input("How many movies do you want to add? "))

for i in range(n):
    name = input("Enter movie name: ")
    budget = int(input("Enter movie budget: "))
    movies.append((name, budget))

total = 0

for movie in movies:
    total += movie[1]

average = total / len(movies)

print("\nAverage Budget:", average)

count = 0

print("\nMovies with higher than average budget:")

for movie in movies:
    if movie[1] > average:
        difference = movie[1] - average
        print(movie[0], "is", difference, "above average")
        count += 1

print("\nNumber of movies above average:", count)