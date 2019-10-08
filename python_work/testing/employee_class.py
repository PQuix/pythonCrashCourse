class Employee():
	"""Creates an employee."""
	
	def __init__(self, first, last, salary):
		"""Defines the employee by name and salary."""
		self.first = first
		self.last = last
		self.salary = salary
	
	def get_full_name(self):
		"""Returns the employee's full name."""
		self.full_name = self.first + " " + self.last
		return self.full_name.title()
	
	def give_raise(self, increase='50000'):
		"""Increases the employee's salary by the specified amount."""
		self.salary = int(self.salary) + int(increase)
		return self.salary
