class Food:

	def __init__(self, inputFoodName):
		self.health_value = [0,50,100,150,200,250]
		self.flavor_value = [0,10,20,30,40,50]
		self.spicy_value = [0,1,2,3,4,5]
		self.__foodName = inputFoodName
		self.__exp = 0
		self.__level = 0

	def show_info(self):
		print("{} \n\tLevel Spicy Food: {}, \n\tHealth: {}, \n\tFlavor: {}, \n\tSpicy: {}".format(
			self.__foodName,
			self.__level,
			self.__health,
			self.__flavor,
			self.__spicy
			)
		)

	@property
	def health_value(self):
		pass

	@property
	def spicy_value(self):
		pass

	@property
	def flavor_value(self):
		pass

	@property
	def levelUp(self):
		pass

	@property
	def gainExp(self):
		pass


	@health_value.setter
	def health_value(self, input):
		self.__health_value = input

	@spicy_value.setter
	def spicy_value(self, input):
		self.__spicy_value = input

	@flavor_value.setter
	def flavor_value(self, input):
		self.__flavor_value = input


	@gainExp.setter
	def gainExp(self,input):
		self.__exp += input
		if(self.__exp >= 100):
			self.levelUp = self.__exp//100
			self.__exp %= 100

	@levelUp.setter
	def levelUp(self,input):
		self.__level += input
		self.__health = self.__health_value[self.__level]
		self.__flavor = self.__flavor_value[self.__level]
		self.__spicy = self.__spicy_value[self.__level]


class FoodSeafood(Food):
	def __init__(self,foodName):
		super().__init__(foodName)
		self.health_value = [0,100,200,300,400,500]
		self.flavor_value = [0,20,40,60,80,100]
		self.spicy_value = [0,2,4,6,8,10,12,14]
		self.levelUp = 1

class FoodTraditionalFood(Food):
	def __init__(self,foodName):
		super().__init__(foodName)
		self.health_value = [0,150,300,450,600,750]
		self.flavor_value = [0,20,40,60,80,100]
		self.spicy_value = [0,3,5,7,9,11,13,15]
		self.levelUp = 1


costumer1 = FoodSeafood('Udang Extra Pedas')
costumer2 = FoodTraditionalFood('Rawon Asam Pedas')

costumer1.show_info()
costumer2.show_info()
