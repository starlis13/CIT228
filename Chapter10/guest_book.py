#10-3
filename = "guest_book.txt"

"""
userName = input("Please enter your full name (q to quit):\n")

with open(filename, "a") as guestFile:
    while userName != 'q':
        guestFile.write(f"\n{userName}")
        print(f"Welcome, {userName}. Thank you for joining us.")
        userName = input("Please enter your full name (q to quit):\n")
"""

import os
import random

if os.path.isfile(filename):
    os.remove(filename)
    
takenRoomNumbers = []
newUserName = input("Please let us know your name (q to quit):\n")

with open(filename, "w") as guestList:
    while newUserName != 'q':
        roomNumber = random.randint(1,50)
        
        while takenRoomNumbers.__contains__(roomNumber) == True:
            roomNumber = random.randint(1,50)
    
        guestAndRoom = f"{newUserName} - Room #{roomNumber}\n"
        guestList.write(guestAndRoom)
        print(f"Hello, {newUserName}. Your room number is {roomNumber}")
        newUserName = input("Please let us know your name (q to quit):\n")

with open(filename) as guestList:
    for guest in guestList:
        print(f"{guest}")