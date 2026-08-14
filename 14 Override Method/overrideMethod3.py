class Food:

	def __init__(self, inputFoodName, inputSpicyLevel):
		self.foodName = inputFoodName
		self.spicy = inputSpicyLevel

	def showInfo(self):
		print("Show Info Class Food")
		print("{} Level Spicy Food: {}".format(
				self.foodName
				self.spicy
			)
		)


class Food_Seafood(Food):
	def __init__(self, inputSeafoodName):
		super().__init__(inputSeafoodName, 100)

	def showInfo(self):
		print("Show Info Sub Class Seafood")
		print("{} \n\tType: Seafood, \n\tLevel Spicy Food: {}".format(self.foodName,self.spicy))
		

class Food_traditinalFood(Food):
	def __init__(self, inputTraditionalFoodName):
		super().__init__(inputTraditionalFoodName, 500)

	def showInfo(self):
		print("Show Info Sub Class Traditional Food")
		print("{} \n\tType: Traditional Food, \n\tLevel Spicy Food: {}".format(self.foodName,self.spicy))

class Food_friedFood(Food):
	def __init__(self, inputFriedFoodName):
		super().__init__(inputFriedFoodName, 200)



costumer1 = Food_Seafood('Bandeng Rica-Rica')
costumer2 = Food_traditinalFood('Rawon Asam Pedas')
costumer3 = Food_traditinalFood('Tempe Penyet')

costumer1.showInfo()
costumer2.showInfo()
costumer3.showInfo()