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

# Chapter 4 --------------
lstCombo = [favoriteFoods[5], favoriteFoods[1], favoriteNumbers[2], favoriteNumbers[4], favoriteMovies[0], favoriteMovies[2]]

print('\n')
print('-------------------------Chapter 4, Hands on 1-------------------------')
print('\n')
print('Food List')
print('-----------------------------------------------------------------------')

for food in favoriteFoods:
    print(f"{food}")

print('\n')
print('Number List')
print('-----------------------------------------------------------------------')

for number in favoriteNumbers:
    print(f"{number}")
    
print('\n')
print('Movie List')
print('-----------------------------------------------------------------------')

for movie in favoriteMovies:
    print(f"{movie}")

print('\n')
print('Combo List')
print('-----------------------------------------------------------------------')

for item in lstCombo:
    print(f"{item}")
