import unittest
import employee


class Test_EmployeeCase(unittest.TestCase):
    def setUp(self):
        self.pavan = employee.Employee('pavan', 'teja', 6000)

    def test_give_default_raise(self):
        amount = self.pavan.give_raise()
        self.assertEqual(amount, 11000)

    def test_give_custom_raise(self):
        amount = self.pavan.give_raise(20000)
        self.assertEqual(amount, 26000)



if __name__ == '__main__':
    unittest.main()