import unittest
from city_functions import get_city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    
    def test_city_country(self):
        """Do city/country pairs like 'Santiago, Chile' work?"""
        formatted_location = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()