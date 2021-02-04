from random import randint

class Die:
    sides = 6
    
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        rolled_value = randint(1, self.sides)
        print(f"Rolled a D{self.sides} and got a {rolled_value}")

counter = 0
d6 = Die()
while counter < 10:
    d6.roll_die()
    counter += 1

counter = 0
d10 = Die(10)
while counter < 10:
    d10.roll_die()
    counter += 1

counter = 0
d20 = Die(20)
while counter < 10:
    d20.roll_die()
    counter += 1