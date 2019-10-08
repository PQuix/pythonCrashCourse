def order_sandwich(*ingredients):
	print("You have ordered a sandwich with:")
	for ingredient in ingredients:
		print("- " + ingredient)

order_sandwich("Bacon", "Lettuce", "Tomato", "Cheese")
