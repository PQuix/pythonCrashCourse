def make_pizza(*toppings):
	"""Make a pizza with all requested toppings"""
	print("Making a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza("Mozzarella")
make_pizza("Mozzarella", "Basil", "Pepperoni")
