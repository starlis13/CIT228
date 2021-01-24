#-----
favoriteFoods = ["pizza", "bibimbap", "ice cream", "long john donut", "steak", "tacos"]
print(f"Favorite Foods: {favoriteFoods}")

favoriteNumbers = [42, 4, 8, 15, 16, 23]
print(f"Favorite Numbers: {favoriteNumbers}")

favoriteMovies = ["Book of Eli", "9", "Nightmare Before Christmas"]
print(f"Favorite Movies: {favoriteMovies}")

print(f"Combo list: {favoriteFoods[5], favoriteFoods[1], favoriteNumbers[2], favoriteNumbers[4], favoriteMovies[0], favoriteMovies[2]}")
print(f"Last Food Item: {favoriteFoods[-1]}")
print(f"2nd, 4th, 6th numbers: {favoriteNumbers[1::2]}")
print(f"All movies: {favoriteMovies}")
print(f"First food, first number, and first movie: {favoriteFoods[0], favoriteNumbers[0], favoriteMovies[0]}")

#-----
favoriteMovies.append("The Mummy")
print(favoriteMovies)

favoriteNumbers.insert(3, 13)
print(favoriteNumbers)

favoriteFoods.insert(5, "Shwarma")
print(favoriteFoods)

del favoriteFoods[-1]
print(favoriteFoods)

favoriteMovies.pop()
print(favoriteMovies)

favoriteNumbers.pop(2)
print(favoriteNumbers)

#-----
favoriteMovies.sort()
print(f"Sorted List: {favoriteMovies}")

favoriteFoods.sort()
print(f"Sorted List: {favoriteFoods}")

print(f"Temp Sorted List: {sorted(favoriteNumbers)}")
print(f"Unsorted List: {favoriteNumbers}")

favoriteMovies.reverse()
print(f"Reverse Sorted: {favoriteMovies}")

#-----
