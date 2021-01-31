#7-8
sandwich_orders = ["Italian", "Panini", "Pizza Sub", "Dessert"]
finished_sandwiches = []

while len(sandwich_orders) > 0:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    
    print(f"I've made your {current_sandwich} sandwich!")
    
print(f"The following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
    
finished_sandwiches.clear()
    
#7-9
sandwich_orders = ["Italian", "Pastrami", "Panini", "Pastrami", "Pizza Sub", "Pastrami", "Dessert"]
print(f"Sadly, the deli has run out of pastrami. All orders containing pastrami will be removed.")

while sandwich_orders.__contains__("Pastrami"):
    sandwich_orders.remove("Pastrami")
    
while len(sandwich_orders) > 0:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    
    print(f"I've made your {current_sandwich} sandwich!")
    
print(f"The following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")