favorite_fruits = ["peach", "apple", "banana"]

if favorite_fruits:
    print("The list exists")

if "peach" in favorite_fruits:
    print("Peach exists in the list")
    
if "cherry" not in favorite_fruits:
    print("The list doesn't have cherry in it")
    
if "apple" in favorite_fruits:
    print("The list has apple in it")
    
if "banana" == favorite_fruits[-1]:
    print("The last item in the list is banana")
