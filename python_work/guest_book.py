filename = 'guestbook.txt'

live = False

def write_to_book():
	live = True
	while live:
		first = input("Please input your name for the guestbook:\nFirst Name: ")
		last = input("Last Name: ")
	
		full_name = first.title() + " " + last.title()
	
		with open(filename, 'a') as guestbook:
			guestbook.write(full_name + "\n")
			
		conti = input("Do you want to add another name?\nY/N\n")
		
		if conti.lower() == 'y':
			live = True
		else:
			live = False
			menu()

def read_from_book():
	with open(filename) as guestbook:
		names = guestbook.readlines()
	
	for name in names:
		print(name.strip())

def menu():
	selection = input("Please choose your action:\n1. Write to Guestbook.\n2. Read from Guestbook\n")
	
	if selection == str(1):
		write_to_book()
	elif selection == str(2):
		read_from_book()
	else:
		print("Cannot recognize input, please try again.")
		menu()
	
menu()
