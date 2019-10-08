current_users = ["John", "thirdrevolt", "admin", "ymentradonsax", "snowowl15"]

new_users = ["bananabyte", "switsnow", "Snowowl15", "pycero", "JOHN"]

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
	if user.lower() in current_users_lower:
		print("Please try a different username, " + user + " is already taken")
	else:
		print("Welcome to my website, " + user + "!")
