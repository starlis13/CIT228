#3-4
guests = ["John Skeet", "McKeel Hagerty", "Dave Chappelle"]
baseMessage = "Dear %s,\nI would like to formally invite to my home for dinner Saturday, January 30, 2021. Please let me know if you plan to attend.\n\nThank you.\n\n"

for guest in guests:
    print(baseMessage%(guest))
    
#3-5
print(f"Unfortunately, {guests[1]} is unable to attend dinner this weekend.")

guests.pop(1)
guests.insert(1, "Morgan Freeman")

for guest in guests:
    print(baseMessage%(guest))
    
#3-6
biggerTableMessage = "Hello there, I've found and purchased a new dining room table that will seat more of us for our lovely evening."
print(biggerTableMessage)

guests.insert(0, "Bill Burr")
guests.insert(2, "Mike Rowe")
guests.append("James Spader")

for guest in guests:
    print(baseMessage%(guest))
    
print(f"Our guest list has {len(guests)} people in it.\n\n")
    
#3-7
print("Hello there, unfortunately, due to unforeseen shipping delays, the dinner table won't arrive in time for this weekend's dinner. I will be in touch to schedule another dinner soon. Thanks for understanding.")

for seatNumber in range(4):
    print(f"Hello, {guests[-1]}. I apologize, but my new dinner table will not arrive in time. I hope you understand that I will have to shorten the guest list. I hope we can reschedule for another time. Thank you.")
    guests.pop()

for guest in guests:
    print(f"\n\nDear {guest}, with the shortage of seating, I've unfortunately been forced into shortening the guest list. You, however, are still invited for dinner this Saturday if you would still like to attend. Please let me know your intentions as soon as possible. Thank you.")

del guests[0]
del guests[0]
print(guests)