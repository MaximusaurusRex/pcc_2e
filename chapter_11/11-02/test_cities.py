import unittest
from city_functions import city_country


class NamesTestClass(unittest.TestCase):

    def test_city_country(self):
        city_test = city_country('santiago', 'chile')
        self.assertEqual(city_test, 'Santiago, Chile')

    def test_city_country_population(self):
        city_test = city_country('santiago', 'chile', 5_614_000)
        self.assertEqual(city_test, 'Santiago, Chile - population 5614000')


if __name__ == '__main__':
    unittest.main()
