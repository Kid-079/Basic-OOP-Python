# Diamond Problem

class Restaurant:

	def available(self):
		print("This Is Restaurant")

class Store(Restaurant):
	pass

class Shop(Restaurant):
	pass

class Warehouse(Store, Shop):
	pass


objects = Warehouse()
objects.available()
# help()
help(objects)