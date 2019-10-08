import unittest
from employee_class import Employee

class TestEmployeeSalary(unittest.TestCase):
	"""Tests for the class Employee."""
	
	def setUp(self):
		"""
		Create an employee and and their values.
		"""
		self.new_employee = Employee('tom', 'gundersen', '400000')
	
	def test_default_raise(self):
		self.new_employee.give_raise()
		self.assertEqual(self.new_employee.salary, 450000)
	
	def test_custom_raise(self):
		self.new_employee.give_raise(80000)
		self.assertEqual(self.new_employee.salary, 480000)

unittest.main()
