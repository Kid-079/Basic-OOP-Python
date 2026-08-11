class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.__foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavorLevel
		self.__spicy = inputSpicyLevel

food1 = Food("Cakalang Pedas Manis", 100, 50, 25)
food2 = Food("Udang Mercon", 150, 100, 50)
food3 = Food("Dendeng Pedas", 200, 150, 80)

print(food1.__dict__)