class Food: # template
	# Class Variable
	total = 0

	def __init__(self, inputName, inputHealth, inputFlavorLevel, inputSpicyLevel)
		self.name = inputName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel
		Food.total += 1
		print("Making Food With Name " + inputName)


food1 = Food("Bubur Gurih", 100, 50, 5) # object / instance
print(Food.total)
food2 = Food("Bubur Kacang", 200, 70, 15)
print(Food.total)
food3 = Food("Bubur Pecel", 500, 90, 25)
print(Food.total)


