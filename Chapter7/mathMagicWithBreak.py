import random

problems = 10
counter = 0
numberCorrect = 0
numberIncorrect = 0

while counter < problems:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    
    yourAnswer = int(input(f"What is the sum of {randNumber1} + {randNumber2}?\n"))
    if correctAnswer == yourAnswer:
        print("Great work! You got it right!")
        numberCorrect += 1
    else:
        print("Well, that doesn't seem right, make sure to double check your work!")
        numberIncorrect += 1
        
    counter += 1
    
    if numberIncorrect > 5:
        print("It seems you're having a bit of trouble. You should talk to a tutor and come back for more practice!")
        break
    
print(f"You answered {numberCorrect}/{problems} correctly!")
print(f"Thanks for playing!")