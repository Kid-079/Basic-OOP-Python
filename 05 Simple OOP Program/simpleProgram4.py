class Food:

	def __init__(self, costumerId, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel)
		# Instance Variable
		self.costumer = costumerId
		self.foodName = inputFoodName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel

	def deliver(self, order):
		print(self.costumer + ' Deliver ' + self.foodName + ' --> ' + order.costumer)

	def receive(self):
		print(order.foodName + ' Receive')

costumer1 = Food('Costumer1', 'Bubur Gurih', 100, 50, 10)
costumer2 = Food('Costumer2', 'Bubur Pecel', 200, 80, 20)

costumer1.receive()
costumer1.deliver(costumer2)
print("\n")
costumer2.receive()
costumer2.deliver(costumer1)