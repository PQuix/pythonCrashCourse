pizza = "not done"
toppings = []

while pizza != "done":
	requested_topping = input("Which topping would you like for your pizza?")
	
	if requested_topping.lower() == "quit":
		print("Your pizza with " + str(toppings) + " is finished!")
		pizza = "done"
	else:
		print(requested_topping.title() + " has been added to your pizza.")
		toppings.append(requested_topping)
