lstSomeAnimals = ["cow", "goat", "chicken", "pig", "duck", "rabbit"]
lstAllAnimals = lstSomeAnimals[:]

lstAllAnimals.append("pheasant")
lstAllAnimals.append("horse")
lstAllAnimals.append("sheep")
lstAllAnimals.append("donkey")

print('------------------Original List----------------------')
for animal in lstSomeAnimals:
    print(animal)
    
print('--------------------New List-------------------------')
for animal in lstAllAnimals:
    print(animal)
    
#Exercise 4-10
print(f"The first three items in the list are: {lstAllAnimals[:3]}")

print(f"Three items from the middle of the list are: {lstAllAnimals[3:6]}")

print(f"The last trhee items in the list are: {lstAllAnimals[-3:]}")