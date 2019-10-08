def get_city_country(city, country, population=''):
	"""
	Returns a formatted city and country combination
	in the form of 'City, Country'.
	"""
	if population:
		city_country = city + ", " + country + " -- " + population
	else:
		city_country = city + ", " + country
	return city_country.title()
