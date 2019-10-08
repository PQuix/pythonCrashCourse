class User():
	"""Defines a user and its properties."""
	
	def __init__(self, first_name, last_name, username, fav_game):
		"""Initializes a user and the required information."""
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.fav_game = fav_game
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
		print("Favorite game: " + self.fav_game)
	
	def greet_user(self):
		"""Gives the user a personalized greeting."""
		print("Greetings, " + self.username + "!")

pquix = User("Pål", "Johansen", "PQuix", "Hellblade")

pquix.describe_user()
pquix.greet_user()
print("Login attempts: " + str(pquix.login_attempts))
pquix.increment_login_attempt()
print("Login attempts: " + str(pquix.login_attempts))
pquix.increment_login_attempt()
print("Login attempts: " + str(pquix.login_attempts))
pquix.increment_login_attempt()
print("Login attempts: " + str(pquix.login_attempts))
pquix.reset_login_attempts()
print("Login attempts: " + str(pquix.login_attempts))
