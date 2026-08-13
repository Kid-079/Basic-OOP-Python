class Food:

	def __init__(self, inputFoodName, inputHealth, inputFlavorLevel, inputSpicyLevel):
		self.foodName = inputFoodName
		self.health = inputHealth
		self.flavor = inputFlavorLevel
		self.spicy = inputSpicyLevel

class Food_Seafood(Food):
	def __init__(self, inputSeafoodName):
		self.seafoodName = inputSeafoodName
		self.spicy = 100

class Food_traditinalFood(Food):
	def __init__(self, inputTraditionalFoodName):
		self.traditionalFoodName = inputTraditionalFoodName
		self.spicy = 500

costumer1 = Food_Seafood('Bandeng Rica-Rica')
costumer2 = Food_traditionalFood('Rawon Asam Pedas')

print(costumer1.foodName , " " , costumer1.spicy)
print(costumer2.foodName , " " , costumer2.spicy)
