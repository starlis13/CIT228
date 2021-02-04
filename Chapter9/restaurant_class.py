#9-1
class Restaurant:
    restaurant_name = ""
    cuisine_type = ""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant serves {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"The restaurant is now open!")
        
        
the_restaurant = Restaurant("Food Place", "dog food")
print(f"We named the restaurant {the_restaurant.restaurant_name}")
print(f"We decided to serve {the_restaurant.cuisine_type}")

the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()


#9-2
second_restaurant = Restaurant("The French", "Japanese food")
third_restaurant = Restaurant("The Rising Sun", "American food")
fourth_restaurant = Restaurant("Stars and Stripes", "Russian food")

second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
fourth_restaurant.describe_restaurant()