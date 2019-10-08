class Restaurant():
	"""A class that represents a restaurant."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name of restaurant and type of cuisine served."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		"""Describes the restaurant."""
		print(self.restaurant_name.title() +
		" is a restaurant that serves " + self.cuisine_type.title())
	
	def open_restaurant(self):
		"""Stating the opening of the restaurant."""
		print(self.restaurant_name.title() + " is now open!")

#restaurant = Restaurant("giornos", "italian")
#print("Restaurant: " + restaurant.restaurant_name.title())
#print("Cuisine: " + restaurant.cuisine_type.title())

#restaurant.describe_restaurant()
#restaurant.open_restaurant()

first = Restaurant("Jennifers", "German")
second = Restaurant("Seconds", "Mystery Food")
third = Restaurant("Freddy Fuego", "Burritos")

first.describe_restaurant()
second.describe_restaurant()
third.describe_restaurant()
