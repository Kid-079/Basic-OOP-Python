from abc import ABC,abstractmethod

class Button(ABC):

	def __init__(self,set_link):
		self.link = set_link

	@abstractmethod
	def click(self):
		pass

class PushButton(Button):

	def click(self):
		# print("Push Button Click")
		# print("Life Is Like Riding Bicycle. To Keep Your Balance, You Must Keep Moving")
		print("Go To: {}".format(self.link))



button1 = PushButton("www.restaurant.com")
button1.click()
