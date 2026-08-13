class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.__foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavor
		self.__spicy = inputSpicyLevel


	def spicyLevel(self):
		return self.__spicy

food1 = Food('Dendeng Pedas', 100, 50, 25)

print(food1.spicyLevel())
