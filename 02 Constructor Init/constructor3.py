class Food: # template
	
	def __init__(self, inputName, inputHealth, inputFlavorLevel, inputSpicyLevel)
		self.name = inputName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel

food1 = Food("Bubur Gurih", 100, 50, 5) # object / instance
food2 = Food("Bubur Kacang", 200, 70, 15)
food3 = Food("Bubur Pecel", 500, 90, 25)

print(food1.name)
print(food2.flavor)
print(food3.spicy)