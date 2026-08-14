class Food:

	def available_Food(self):
		print("This is Food")

class Drink:

	def available_Drink(self):
		print("This is Drink")

class Restaurant(Food,Drink):
	pass


objects = Restaurant()

objects.available_Food()
objects.available_Drink()