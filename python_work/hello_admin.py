usernames = ["pquix", "thirdrevolt", "admin", "ymentradonsax", "snowowl15"]

if usernames:
	for user in usernames:
		if(user == "admin"):
			print("Greetings, " + user.title() + ", would you like to see a status report?")
		else:
			print("Hello, " + user.title() + ", thank you for logging in.")
else:
	print("Sorry, there are no users registered...")
