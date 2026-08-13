class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.foodName = inputFoodName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel

class Food_Seafood:
	pass

costumer1 = Food('Dendeng Mercon', 100, 25, 10)
costumer2 = Food_Seafood()

print(costumer1.foodName)
# print(costumer2.foodName)
# print(costumer2.__dict__)
# print(help(costumer2))