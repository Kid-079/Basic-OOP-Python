class Food:

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicy = inputSpicyLevel
		# self.health = inputHealth
		# self.flavor = inputFlavorLevel

class Food_Seafood(Food):
	def __init__(self, inputSeafoodName):
		# Food.__init__(self, inputSeafoodName, 100)
		super().__init__(inputSeafoodName, 100)

class Food_traditinalFood(Food):
	def __init__(self, inputTraditionalFoodName):
		# Food.__init__(self, inputTraditionalFoodName, 500)
		super().__init__(inputTraditionalFoodName, 500)

costumer1 = Food_Seafood('Bandeng Rica-Rica')
costumer2 = Food_traditionalFood('Rawon Asam Pedas')

print(costumer1.foodName , " " , costumer1.spicy)
print(costumer2.foodName , " " , costumer2.spicy)
