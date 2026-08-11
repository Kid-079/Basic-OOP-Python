class Food:

	# Private Class Variable
	__total = 0

	def __init__(self, inputFoodName):
		self.__foodName = inputFoodName
		Food.__total += 10

	# Method Just Applies With Object
	def getTotal(self):
		return Food.__total

	# Method Not Applies With Object But Applies With Class
	def getTotal1():
		return Food.__total

	# Method Static (Decorator)
	@staticmethod
	def getTotal2():
		return Food.__total


food1 = Food('Udang Mercon')
# print(Food.__total)
# print(food1.getTotal())
print(Food.getTotal2())
food2 = Food('Dendeng Pedas')
print(food2.getTotal2())
food3 = Food('Bandeng Rica-Rica')
print(food3.getTotal2())