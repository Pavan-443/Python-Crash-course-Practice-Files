import unittest
import city_functions111


class CityCountry_Testcase(unittest.TestCase):
    def test_citycountry(self):
        message = city_functions111.print_citycountry('Hyderabad', 'India')
        self.assertEqual(message.lower(), 'hyderabad, india')

    def test_citycountrypopulation(self):
        message = city_functions111.print_citycountry('Hyderabad', 'India', 50000)
        self.assertEqual(message.lower(), 'hyderabad, india, population -50000')


if __name__ == '__main__':
    unittest.main()
