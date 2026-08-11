class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.__foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavorLevel
		self.__spicy = inputSpicyLevel

	# Getter
	def getName(self):
		return self.__foodName

# Start Game
food1 = Food("Cakalang Pedas Manis", 100, 50, 25)
food2 = Food("Udang Mercon", 150, 100, 50)
food3 = Food("Dendeng Pedas", 200, 150, 80)

# Game On Play
print(food1.getName())
print(food2.getName())
print(food3.getName())