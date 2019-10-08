class User():
	"""Defines a user and its properties."""
	
	def __init__(self, first_name, last_name, username):
		"""Initializes a user and the required information."""
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.login_attempts = 0
	
	def full_name(self):
		"""Sets the users full name."""
		full_name = self.first_name + " " + self.last_name
		return full_name
	
	def increment_login_attempt(self):
		"""Increments login attempts by 1."""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""Resets login attempts to 0."""
		self.login_attempts = 0
	
	def describe_user(self):
		"""Lists the users information."""
		print("Name: " + self.full_name())
		print("Username: " + self.username)
	
	def greet_user(self):
		"""Gives the user a personalized greeting."""
		print("Greetings, " + self.username + "!")
