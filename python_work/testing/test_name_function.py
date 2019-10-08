import unittest
from name_function import get_formatted_name as gfn

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""
	
	def test_first_last_name(self):
		"""Do names like 'Jotaro Kujo' work?"""
		formatted_name = gfn('jotaro', 'kujo')
		self.assertEqual(formatted_name, 'Jotaro Kujo')
	
	def test_first_last_middle_name(self):
		"""Do names like 'Giorno Dio Giovanna' work?"""
		formatted_name = gfn('giorno', 'giovanna', 'dio')
		self.assertEqual(formatted_name, 'Giorno Dio Giovanna')

unittest.main()
