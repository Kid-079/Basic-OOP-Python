class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.foodName = inputFoodName
		self.__health = inputHealth
		self.__flavor = inputFlavor
		self.__foodName = inputSpicyLevel
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

	@flavor.setter
	def flavor(self, input):
		self.__flavor = input

	@flavor.deleter
	def flavor(self):
		print('Delete Flavor')
		self.__flavor = None

food1 = Food('Dendeng Pedas', 100, 50, 25)

print('Change Info')
print(food1.info)
# print(food1.__dict__)

food1.foodName = "Telur Balado"
print(food1.info)
print("\n")

print("Getter And Setter For __flavor")
print(food1.flavor)
print(food1.__dict__)
print("\n")

food1.flavor = 100 # NO ERROR --> USE SETTER TO CHANGE VARIABLE
print(food1.flavor)
print(food1.__dict__)
print("\n")

print('flavor deleted')
del food1.flavor
print(food1.__dict__)