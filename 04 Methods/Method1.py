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

food1 = Food('Bubur Gurih', 100, 25, 5)
food2 = Food('Bubur Pecel', 500, 50, 10)

print(food1.__dict__)
print(food2.__dict__)