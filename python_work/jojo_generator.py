print("W E L C O M E   T O   T H E   J O J O   G E N E R A T O R ! ! !")
first = input("Please state your first name:\n")
last = input("Then your last name:\n")

full_name = first + " " + last

first_first_jo = first[:2]
first_last_jo = first[-2:]
last_first_jo = last[:2]
last_last_jo = last[-2:]

if first_first_jo.lower() == 'jo' and last_first_jo.lower() == 'jo':
	print(full_name.title() + " is indeed a JoJo!")
elif first_first_jo.lower() == 'jo' and last_last_jo.lower() == 'jo':
	print(full_name.title() + " is indeed a JoJo!")
else:
	print("Weak... " + full_name.title() + " is not a JoJo...")
