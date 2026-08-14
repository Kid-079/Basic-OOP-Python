class Food:

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicy = inputSpicyLevel
		# self.health = inputHealth
		# self.flavor = inputFlavorLevel

	def showInfo(self):
		print("{} - Level Spicy Food: --> {}".format(self.foodName,self.spicy))

class Food_Seafood(Food):
	def __init__(self, inputSeafoodName):
		# Food.__init__(self, inputSeafoodName, 100)
		super().__init__(inputSeafoodName, 100)
		super().showInfo()
		# Food.showInfo(self)

class Food_traditinalFood(Food):
	def __init__(self, inputTraditionalFoodName):
		# Food.__init__(self, inputTraditionalFoodName, 200)
		super().__init__(inputTraditionalFoodName, 200)
		super().showInfo()
		# Food.showInfo(self)

costumer1 = Food_Seafood('Bandeng Rica-Rica')
costumer2 = Food_traditionalFood('Rawon Asam Pedas')

# print(costumer1.foodName , " " , costumer1.spicy)
# print(costumer2.foodName , " " , costumer2.spicy)
