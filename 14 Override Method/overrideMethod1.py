class Food:

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicy = inputSpicyLevel

	def showInfo(self):
		print("{} Level Spicy Food: {}".format(self.foodName,self.spicy))


class Food_Seafood(Food):
	def __init__(self, inputSeafoodName):
		super().__init__(inputSeafoodName, 100)

class Food_traditinalFood(Food):
	def __init__(self, inputTraditionalFoodName):
		super().__init__(inputTraditionalFoodName, 500)


costumer1 = Food_Seafood('Bandeng Rica-Rica')
costumer2 = Food_traditinalFood('Rawon Asam Pedas')

costumer1.showInfo()
costumer2.showInfo()