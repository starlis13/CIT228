#9-1
class Restaurant:
    restaurant_name = ""
    cuisine_type = ""
    number_served = 0
    
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant serves {self.cuisine_type}")
        print(f"The restaurant has served {self.number_served} people")
        
    def open_restaurant(self):
        print(f"The restaurant is now open!")
        
    def set_number_served(self, number_served):
        if number_served > -1:
            self.number_served = number_served
            
    def increment_number_served(self, increment_by):
        self.number_served += increment_by
        
        
restaurant = Restaurant("Food Place", "dog food")
print(f"We named the restaurant {restaurant.restaurant_name}")
print(f"We decided to serve {restaurant.cuisine_type}")
print(f"We have proudly served {restaurant.number_served} people!")
restaurant.number_served = 3
print(f"We have hesitantly served {restaurant.number_served} people!")

restaurant.set_number_served(1)
print(f"Sorry, that was a mistake earlier, we've actually served {restaurant.number_served} people!")

restaurant.increment_number_served(93)
print(f"Can you believe that {restaurant.number_served} people decided to get food poisoning from us today?")