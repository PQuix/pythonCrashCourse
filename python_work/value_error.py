while True:
	dividend = input("Give me a number:\n")
	if dividend.lower() == 'q':
		break
	divisor = input("And another one:\n")
	if divisor.lower() == 'q':
		break
	
	try:
		answer = int(dividend) / int(divisor)
	except ValueError:
		print("One of your inputs contain text, please try again.")
	except ZeroDivisionError:
		print("You can't divide by zero, please try again.")
	else:
		print(answer)
