txtUserChosenNumber = input("Please choose a number:\n")

try:
    numValue = float(txtUserChosenNumber)
    
    if numValue % 10 == 0:
        print("Your number is a multiple of 10!")
    else:
        print("Sadly, you've chosen a number that is NOT a multiple of 10!")
        
except ValueError:
    print("Your entry was invalid")