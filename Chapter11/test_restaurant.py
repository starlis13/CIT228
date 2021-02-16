import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        restaurant_name = "Cafe Fromage"
        cuisine_type = "Mongolian"
        number_served = 1000
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)
    
    def test_set_number_served_integer(self):
        new_number_served = 56
        self.restaurant.set_number_served(new_number_served)
        self.assertEqual(56, self.restaurant.number_served)

    def test_set_number_served_string(self):
        new_number_served = "998"
        self.restaurant.set_number_served(new_number_served)
        self.assertEqual(998, self.restaurant.number_served)
    
    def test_increment_number_served_integer(self):
        increment_number_by = 16
        self.restaurant.increment_number_served(increment_number_by)
        self.assertEqual(1016, self.restaurant.number_served)
        
    
    def test_increment_number_served_string(self):
        increment_number_by = "4815161342"
        self.restaurant.increment_number_served(increment_number_by)
        self.assertEqual(4815162342, self.restaurant.number_served)
        
if __name__ == "__main__":
    unittest.main()