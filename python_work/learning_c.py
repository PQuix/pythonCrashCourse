filename = 'python_abilities.txt'

with open(filename) as python:
	abilities = python.readlines()

for lines in abilities:
	fixed = lines.replace('Python', 'C')
	print(fixed)

