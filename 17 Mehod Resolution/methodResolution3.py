# Method Resolution Order // Multiple Inheritance

class Food:

	def available(self):
		print("This is Food")

class Drink:

	def available(self):
		print("This is Drink")

class Restaurant(Food,Drink):
	
	def available(self):
		pass


objects = Restaurant()

objects.available()
# help()
help(objects)