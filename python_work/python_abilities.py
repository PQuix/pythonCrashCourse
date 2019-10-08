filename = 'python_abilities.txt'

with open(filename) as python:
	abilities = python.readlines()

for lines in abilities:
	print(lines.strip())
