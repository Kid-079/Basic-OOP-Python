class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.__foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavor
		self.__spicy = inputSpicyLevel
		self.info = "Food Name {} : \n\tSpicy Level {}".format(self.__foodName, self.__spicy)

	def spicyLevel(self):
		return self.__spicy

food1 = Food('Dendeng Pedas', 100, 50, 25)

print(food1.info)
food1.info = "Information"

print(food1.info)
