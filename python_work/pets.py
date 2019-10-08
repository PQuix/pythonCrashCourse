pets = {
	'miescha': {
		'type': 'cat',
		'gender': 'male',
		'owner': 'jennifer',
		'status': 'grumpy',
		},
	'dima': {
		'type': 'dog',
		'gender': 'male',
		'owner': 'tony',
		'status': 'scared',
		},
	'maya': {
		'type': 'cat',
		'gender': 'female',
		'owner': 'jennifer',
		'status': 'scared',
		},
	}

for name, info in pets.items():
	animal_type = info['type']
	owner = info['owner']
	mood = info['status']
	gender = info['gender']
	if gender == "male":
		pronoun = "he"
	else:
		pronoun = "she"
	
	print(name.title() + " is a " + animal_type + " and is owned by " +
	owner.title() + ". " + pronoun.title() + " is usually a bit " +
	mood + "...")
