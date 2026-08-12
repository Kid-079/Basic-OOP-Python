class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavor
		self.__foodName = inputSpicyLevel
		# self.info = "Food Name {} : \n\tSpicy Level {}".format(self.__foodName, self.__spicy)

	@property
	def info(self):
		# return "Food Name {} : \n\tSpicy Level {}".format(self.__foodName, self.__spicy)
		return "Food Name {} : \n\tSpicy Level {}".format(self.foodName, self.__spicy)


food1 = Food('Dendeng Pedas', 100, 50, 25)

print(food1.info)
print(food1.__dict__)

food1.foodName = "Terung Rica-Rica"

print(food1.info)