class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel)
		# Instance Variable
		self.foodName = inputFoodName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel

	def deliver(self):
		print('Delivery --> ' + self.foodName)

	def receive(self):
		print(self.foodName + ' Receive')

costumer1 = Food('Bubur Gurih', 100, 50, 10)
costumer2 = Food('Bubur Pecel', 200, 80, 20)

costumer1.deliver()