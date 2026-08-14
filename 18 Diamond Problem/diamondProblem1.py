# Diamond Problem

class Restaurant:

	def available(self):
		print("This Is Restaurant")

class Store(Restaurant):

	def available(self):
		print("This Is Store")

class Shop(Restaurant):

	def available(self):
		print("This Is Shop")

class Warehouse(Store, Shop):
	pass


objects = Warehouse()
objects.available()
# help()
help(objects)