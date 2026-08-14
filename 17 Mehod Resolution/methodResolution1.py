# Method Resolution Order // Multiple Inheritance

class Food:

	def available(self):
		print("This is Food")

class Drink:

	def available(self):
		print("This is Drink")

class Restaurant(Food,Drink):
	pass


objects = Restaurant()

objects.available()
