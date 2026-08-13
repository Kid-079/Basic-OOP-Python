class Food:

	# Private Class Variable
	__total = 0

	def __init__(self, inputFoodName, Health, FlavorLevel, SpicyLevel):
		self.__foodName = inputFoodName
		self.__healthDefault = Health
		self.__flavorDefault = FlavorLevel
		self.__spicyDefault = SpicyLevel
		self.__level = 1
		self.__exp = 0

		self.__healthMax = self.__healthDefault * self.__level
		self.__spicy = self.__spicyDefault * self.__level
		self.__flavor = self.__flavorDefault * self.__level

		self.__health = self.__healthMax

		Food.__total += 1


	@property
	def info(self):
		return "{} level {}: \n\thealth = {}/{} \n\tspicy = {} \n\tflavor = {}".format(self.__foodName, self.__level, self.__health, self.__healthMax, self.__spicy, self.__flavor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self, addExp):
		self.__exp += addExp
		if (self.__exp >= 100):
			print(self.__foodName, 'level up')
			self.__level += 1
			self.__exp -= 100

			self.__healthMax = self.__healthDefault * self.__level
			self.__spicy = self.__spicyDefault * self.__level
			self.__flavor = self.__flavorDefault * self.__level


costumer1 = Food('Bubur Pedas', 100, 50, 35)
costumer2 = Food('Dendeng Mercon', 100, 25, 50)
print(costumer1.info)


costumer1.gainExp = 10
costumer1.gainExp = 20
costumer1.gainExp = 30
costumer1.gainExp = 40
costumer1.gainExp = 50
# print(costumer1.__dict__)
print(costumer1.info)