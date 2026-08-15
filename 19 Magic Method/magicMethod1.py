class Bubur:
	
	# Magic Method
	def __init__(self,inputBuburName,inputSpicyLevel):
		self.buburName = inputBuburName
		self.spicy = inputSpicyLevel

Menu1 = Bubur("Kacang Gurih Pedas", 50)
Menu2 = Bubur("Pecel Mercon", 30)
Menu3 = Bubur("Ayam Suwir", 70)
print(Menu1.buburName)
print(Menu2.buburName)
print(Menu3.buburName)
