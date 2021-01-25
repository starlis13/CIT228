# Hands on Chapter 4 numbers
import random

randNumber = random.randrange(10, 100)

lstRandomNumbers = []

for index in range(randNumber):
    lstRandomNumbers.append(random.randrange(10, 100))
    
print(lstRandomNumbers)

lstRandomNumbers.sort()

print(f"The largest number = {lstRandomNumbers[-1]}")
print(f"The smallest number = {lstRandomNumbers[0]}")
print(f"The total of all numbers = {sum(lstRandomNumbers)}")
print(f"The average number = {sum(lstRandomNumbers)/len(lstRandomNumbers)}")