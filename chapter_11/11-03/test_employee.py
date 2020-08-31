import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.example = Employee('Tim', 'Apple', 20000)

    def test_give_default_raise(self):
        self.example.give_salary()
        self.assertEqual(self.example.salary, 25000)

    def test_give_custom_raise(self):
        self.example.give_salary(10000)
        self.assertEqual(self.example.salary, 30000)


if __name__ == '__main__':
    unittest.main()
