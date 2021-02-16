import unittest
from city_functions import FormatCountryCity

class TestCities(unittest.TestCase):
    def test_city_country(self):
        country = "Russia"
        city = "Volgograd"
        self.assertEqual(f"{city}, {country}", FormatCountryCity(country, city))
        
    def test_city_country_population(self):
        country = "Russia"
        city = "Volgograd"
        population = "1019000"
        self.assertEqual(f"{city}, {country} - Population: {population}", FormatCountryCity(country, city, population))
        
if __name__ == "__main__":
    unittest.main()