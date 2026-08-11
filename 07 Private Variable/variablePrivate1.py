class Food:

	# Class Variable
	total = 0

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicyLevel = inputSpicyLevel

food1 = Food("Terung Rica-Rica", 50)
food2 = Food("Cumi Pedas", 50)

print(food1.__dict__)
print(food2.__dict__)
print("\n")
print(food1.foodName)
print(food1.spicyLevel)
print("\n")
print(food2.foodName)
print(food2.spicyLevel)