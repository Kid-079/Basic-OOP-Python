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

bubur_gurih = Food('Bubur Gurih', 100, 50, 10)
bubur_pecel = Food('Bubur Pecel', 200, 80, 20)

bubur_gurih.deliver()