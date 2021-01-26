current_users = ["user1", "user2", "user3", "user4", "User5"]
new_users = [current_users[0], current_users[1]]

for index in range(0, len(current_users)-1):
    current_users[index] = current_users[index].lower()
    
new_users.append("user6")
new_users.append("user7")
new_users.append("user8")

for user in new_users:
    if user.lower() in current_users:
        print("This username is invalid. Please enter a new one.")
    else:
        print("Your username is acceptable")
