group_size = input("Welcome to Jennifer's! How many people is in your group tonight?\n")
if int(group_size) < 8:
	print("Oh, you are only " + group_size + " people. Your table is right this way!")
else:
	print("I'm sorry, we don't have any tables available for " + group_size + " people.")
	wait = input("Would you like to wait for one?\n")
	if wait.lower() == "yes":
		print("Very well. Please be seated by the bar while you wait.")
	else:
		print("I'm sorry for the inconvenience. Please come again at another time.")
