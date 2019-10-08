def make_car(make, model, **additional):
	car = {}
	car['make'] = make
	car['model'] = model
	for key, value in additional.items():
		car[key] = value
	return car

car = make_car("subaru", "outback", color='blue', sunroof='no')
print(car)
car = make_car("saab", "9-5", color='black', sunroof='no', stereo='yes')
print(car)
