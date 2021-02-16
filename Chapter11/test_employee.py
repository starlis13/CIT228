import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        firstName = "Allido"
        lastName = "Iswin"
        salary = 95000
        self.test_employee = Employee(firstName, lastName, salary)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(100000, self.test_employee.get_salary())
    
    def test_give_custom_raise(self):
        increase = 2750
        self.test_employee.give_raise(increase)
        self.assertEqual(97750, self.test_employee.get_salary())
    
if __name__ == "__main__":
    unittest.main()