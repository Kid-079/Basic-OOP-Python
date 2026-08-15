class Bubur:
	
	# Magic Method
	def __init__(self,inputBuburName,inputSpicyLevel):
		self.buburName = inputBuburName
		self.spicy = inputSpicyLevel

	def __repr__(self):
		return "Bubur : {} With Spicy Level : {}".format(self.buburName)

Menu1 = Bubur("Kacang Gurih Pedas", 50)
Menu2 = Bubur("Pecel Mercon", 30)
Menu3 = Bubur("Ayam Suwir", 70)
print(Menu1)
print(Menu2)
print(Menu3)