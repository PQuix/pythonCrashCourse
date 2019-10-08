def show_magicians(great_magicians):
	for magician in great_magicians:
		print(magician)

def make_great(magicians):
	while magicians:
		great_magician = magicians.pop()
		
		great_magician += " the Great"
		great_magicians.append(great_magician)

magicians = ["Bob Ross", "Gemini", "Kvothe"]
great_magicians = []
make_great(magicians)
show_magicians(great_magicians)
