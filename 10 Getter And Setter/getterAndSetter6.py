class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavor
		self.__spicy = inputSpicyLevel
		# self.info = "Food Name {} : \n\tSpicy Level {}".format(self.foodName, self.__spicy)
		# self.__info = ""Food Name {} : \n\tSpicy Level {}".format(self.__foodName, self.__spicy)

	@property
	def info(self):
		# return self.__info
		return "Food Name {} : \n\tSpicy Level {}".format(self.foodName, self.__spicy)
		# return "Food Name {} : \n\tSpicy Level {}".format(self.__foodName, self.__spicy)

	@property
	def flavor(self):
		pass

	@flavor.getter
	def flavor(self):
		return self.__flavor

food1 = Food('Dendeng Pedas', 100, 50, 25)

print('Change Info')
print(food1.info)
# print(food1.__dict__)

food1.foodName = "Telur Balado"
print(food1.info)

print("Getter And Setter For __flavor")
print(food1.flavor)
food1.flavor = 100 # ERROR CAUSE PRIVATE VARIABLE
