class Food:

	# Private Class Variable
	__total = 0

	def __init__(self, inputFoodName):
		self.__foodName = inputFoodName
		Food.__total += 10

	# Method Just Applies With Object
	def getTotal(self):
		return Food.__total

food1 = Food('Udang Mercon')
# print(Food.__total)
print(food1.getTotal())
food2 = Food('Dendeng Pedas')
food3 = Food('Bandeng Rica-Rica')
