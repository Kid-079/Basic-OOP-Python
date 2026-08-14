class Restaurant:

	def setRestaurant(self, inputRestaurant):
		self.restaurant = inputRestaurant

	def showRestaurant(self):
		print(self.inputRestaurant)


class Type_Food:
	def setType(self, inputTypeFood):
		self.typeFood = inputTypeFood

	def showType(self):
		print(self.typeFood)


class Food(Restaurant,Type_Food):

	def __init__(self, inputFoodName, inputHealth, inputSpicyLevel, inputFlavorLevel):
		self.foodName = inputFoodName
		self.health = inputHealth
		self.spicy = inputSpicyLevel
		self.flavor = inputFlavorLevel

costumer1 = Food('Dendeng Pedas Gurih', 100, 50, 10)
costumer2 = Food('Rawon Asam Pedas', 200, 75, 20)

costumer1.setRestaurant("Seafood Restaurant")
costumer1.setType("Seafood")

costumer1.showRestaurant()
costumer1.showType()
