from user_class import User

class Admin(User):
	"""Defines an admin, child of the User-class, and its properties."""
	
	def __init__(self, first_name, last_name, username):
		"""Initializes the admin and the required information."""
		super().__init__(first_name, last_name, username)
		self.privileges = Privileges(
				"Can add posts",
				"Can delete posts",
				"Can ban users"
				)

class Privileges():
	"""Defines a list of privileges for a user."""
	
	def __init__(self, *privileges):
		self.privileges = privileges
	
	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)
