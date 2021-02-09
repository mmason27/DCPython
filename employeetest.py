from employee import Employee
import unittest

class EmployeeTests(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Megan", "Mason", 0) 

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(5000, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(10000, self.employee.salary)

    def tearDown(self):
        print("TEAR DOWN")

unittest.main()









