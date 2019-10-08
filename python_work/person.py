people = {
	'jennifer': {
		'first': 'jennifer',
		'last': 'elsner',
		'location': 'hannover, germany',
		},
	'torgeir': {
		'first': 'torgeir julian',
		'last': 'hanssen',
		'location': 'alta, norway',
		},
	'paal': {
		'first': 'pål krister',
		'last': 'johansen',
		'location': 'oslo, norway',
		},
	}

for info in people.values():
	full_name = info['first'] + " " + info['last']
	location = info['location']
	
	print(full_name.title() + " lives in " + location.title())
