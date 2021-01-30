# Try it yourself 6-2
dictFavoriteNumbers = {
    "Eli":59,
    "Amanda":27,
    "Laura":16,
    "Isaac":92,
    "Steven":1024
}

for val in dictFavoriteNumbers:
    print(f"{val}'s favorite number is {dictFavoriteNumbers.get(val)}")

    