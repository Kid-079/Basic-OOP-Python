class Bubur:
	
	# Magic Method
	def __init__(self,inputBuburName,inputSpicyLevel):
		self.buburName = inputBuburName
		self.spicy = inputSpicyLevel

	def __repr__(self):
		return "DEBUG: Bubur : {} With Spicy Level : {}".format(self.buburName,self.spicy)

	def __str__(self):
		return "PRODUCTION: Bubur : {} With Spicy Level : {}".format(self.buburName,self.spicy)

	def __add__(self,objects):
		return self.spicy + objects.spicy

	@property
	def __dict__(self):
		return "This Object Have Name And Level Spicy Food"


Menu1 = Bubur("Kacang Gurih Pedas", 50)
Menu2 = Bubur("Pecel Mercon", 30)
Menu3 = Bubur("Ayam Suwir", 70)
print(repr(Menu1))
print(Menu2)
print(Menu3)
print(Menu2 + Menu3)
print(Menu2.__dict__)
print(Menu2.__dict__)