#Exercise 5-8
lstUsernames = ["sstarlin", "ssterling", "sstarling", "sstarline", "admin"]

#lstUsernames.clear()

if len(lstUsernames) == 0:
    print("We need to find some users!")

for user in lstUsernames:
    if user == "admin":
        print(f"Hey {user}, I hope you're having a good day!")
    else:
        print(f"Greetings, {user}.")
