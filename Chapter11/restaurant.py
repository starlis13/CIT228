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
        try:
            number_served = int(number_served)
        except:
            pass
        else:
            if number_served > -1:
                self.number_served = number_served
            
    def increment_number_served(self, increment_by):
        try:
            increment_by = int(increment_by)
        except:
            pass
        else:
            self.number_served += increment_by