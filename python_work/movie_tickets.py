while True:
	age = input("Welcome to Jennifer's Cinema!\n" +
	"One ticket?\n" + "Coming right up!\n" +
	"How old are you?\n")
	
	if age.lower() == "quit":
		break
	
	if int(age) < 3:
		print("I'm sorry, babies are not allowed into the cinema...\n" +
		"NEXT!\n")
	elif int(age) < 12:
		print("Children are also not allowed, NEXT!\n")
	elif int(age) < 20:
		print(age + " huh? You look like a punk... That'll be " +
		"$13, but I'm keeping my eye on you...\nNEXT!\n")
	else:
		print("Alright, that'll be $15, thank you very much.\n" +
		"NEXT!\n")
