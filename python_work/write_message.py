filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I love appending and not overwriting!\n")
