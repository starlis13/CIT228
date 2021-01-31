import random

numberCorrect = 0
keepPlaying = True

while keepPlaying:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    
    yourAnswer = int(input(f"What is the sum of {randNumber1} + {randNumber2}?\n"))
    
    if correctAnswer == yourAnswer:
        print("Great work! You got it right!")
        numberCorrect += 1
    else:
        print("Well, that doesn't seem right, make sure to double check your work!")
    
    keepPlaying = input("Would you like to keep going?\n\nEnter 'q' to quit, any key to continue playing!").lower() != "q"
        
        
print(f"You answered {numberCorrect} correctly!")
print(f"Thanks for playing!")