class Food:
	# Class Variable
	total_food = 0

	def __init__(self, inputName, inputHealth, inputFlavorLevel, inputSpicyLevel)
		# Instance Variable
		self.name = inputName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel
		Food.total_food += 1

	# Void Function, Method Without Return and Argument
	def type(self):
		print("Food Name Is " + self.name)

	# Method With Argument, Without Return
	def spicyLevelUp(self, upSpicy):
		self.spicy += upSpicy

food1 = Food('Bubur Gurih', 100, 25, 5)
food2 = Food('Bubur Pecel', 500, 50, 10)

food1.type()
food1.spicyLevelUp(15)

print(food1.spicy)