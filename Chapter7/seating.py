#7-2
txtResponse = input("Please let us know how many will be dining in your party tonight.\n")

try:
    intResponse = int(txtResponse)
    
    if intResponse > 8:
        print("It seems all of our large tables are occupied for the moment. Please wait for a few minutes as we open a table for you.")
    else:
        print("Your table is ready")
except ValueError:
    print("Please be sure to enter a valid number in your next request for a table.")