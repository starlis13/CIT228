# Exercise 4-8
print("I can't believe I'm making cubes. Borg would be pleased.")
cubes = []

for number in range(1,11):
    print(number * number * number)
    
# Exercise 4-9
print('')
print("Now do it as a comprehension!")
cubes = [value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)
