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
		order.receive(self, self.spicy)

	def receive(self, order, spicyLevel_order):
		print(self.costumer + ' Receive ' + order.foodName)
		spicy_food = spicyLevel_order/self.flavor
		print('Food Spicy Level : ' + str(spicy_food))
		self.health -= spicy_food
		print('Health ' + self.foodName + ' trace ' + str(self.health))


costumer1 = Food('Costumer1', 'Bubur Gurih', 100, 50, 10)
costumer2 = Food('Costumer2', 'Bubur Pecel', 100, 80, 20)

costumer1.deliver(costumer2)
print("\n")
costumer2.deliver(costumer1)
print("\n")
costumer1.deliver(costumer2)
print("\n")
costumer2.deliver(costumer1)
print("\n")
costumer1.deliver(costumer2)
print("\n")
costumer2.deliver(costumer1)
print("\n")
costumer1.deliver(costumer2)
print("\n")
costumer2.deliver(costumer1)
print("\n")
costumer1.deliver(costumer2)
print("\n")
costumer2.deliver(costumer1)