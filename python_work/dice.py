from random import randint

class Die():
	"""Defines a die with variable sides."""
	
	def __init__(self, sides=6):
		"""
		Initializes a die.
		The default number if sides are set to 6 if not otherwise specified.
		"""
		self.sides = sides
	
	def roll_die(self):
		result = randint(1,6)
		print(result)

roll = 1
sixes = Die()
tenner = Die(10)
twenty = Die(20)
for side in range(1,21):
	print("Dice 1 (Ten), roll #" + str(roll) + ":")
	tenner.roll_die()
	print("Dice 2 (Twenty), roll #" + str(roll) + ":")
	twenty.roll_die()
	roll += 1
