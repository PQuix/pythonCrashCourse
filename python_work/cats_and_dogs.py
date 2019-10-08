filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename, encoding='utf-8') as active_file:
			contents = active_file.read()
	except FileNotFoundError:
		pass
	else:
		print(filename + ":")
		print(contents)
