#10-6
quitEntryChar = "q"
operandOne = input(f"Please enter an number ({quitEntryChar} to quit)\n")
operandTwo = input(f"Please enter another number ({quitEntryChar} to quit)\n")

# while loop introduced in 10-7
while operandOne != quitEntryChar and operandTwo != quitEntryChar:
    try:
        result = int(operandOne) + int(operandTwo)
    except ValueError:
        print("You've not entered a number\n")
    else:
        print(f"{operandOne} + {operandTwo} = {result}\n")
    finally:
        operandOne = input(f"Please enter an number ({quitEntryChar} to quit)\n")
        operandTwo = input(f"Please enter another number ({quitEntryChar} to quit)\n")