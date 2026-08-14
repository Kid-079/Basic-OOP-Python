class Food:

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicy = inputSpicyLevel

	def showInfo(self,type):
		print("{} \n\tType: {}, \n\tLevel Spicy Food: {}".format(
				self.foodName,
				type
				self.spicy
			)
		)


class Food_Seafood(Food):
	def __init__(self, inputSeafoodName):
		super().__init__(inputSeafoodName, 100)

	def showInfo(self):
		super().showInfo('Seafood')

class Food_traditinalFood(Food):
	def __init__(self, inputTraditionalFoodName):
		super().__init__(inputTraditionalFoodName, 500)

	def showInfo(self):
		super().showInfo('Traditional Food')


costumer1 = Food_Seafood('Bandeng Rica-Rica')
costumer2 = Food_traditinalFood('Rawon Asam Pedas')

costumer1.showInfo()
costumer2.showInfo()