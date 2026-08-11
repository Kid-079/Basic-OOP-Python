class Food:

	# Class Variable
	total = 0

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicyLevel = inputSpicyLevel

		# Variable Instance Private
		self.__private = "Private"

		# Variable Instance Protected
		self._protected = "Protected" 

food1 = Food("Terung Rica-Rica", 50)
food2 = Food("Cumi Pedas", 50)

print(food1.__dict__)
print(food1.__dict__)
