import unittest
from city_functions import get_city_country as gcc

class CityTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""
	
	def test_city_country(self):
		"""Does combinations like 'Venice, Italy' work?"""
		city_country = gcc('venice', 'italy')
		self.assertEqual(city_country, 'Venice, Italy')
	
	def test_city_country_population(self):
		"""Does combinations like 'Harstad, Norway -- 30000' work?"""
		city_population = gcc('harstad', 'norway', '30000')
		self.assertEqual(city_population, 'Harstad, Norway -- 30000')

unittest.main()
