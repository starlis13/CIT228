from restaurant import Restaurant

class IceCreamStand(Restaurant):
    flavors = []
    
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors
        
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"We have {flavor} is stock")