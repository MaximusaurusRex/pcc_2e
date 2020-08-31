import unittest
from city_functions import city_country


class NamesTestClass(unittest.TestCase):

    def test_city_country(self):
        city_test = city_country('santiago', 'chile')
        self.assertEqual(city_test, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
