# Create Class Abstract
# abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC):

	@abstractmethod
	def click(self):
		# print("Button Click")
		# print("You Will Grow Beautifully In Your Own Way")
		# print("The Only Thing Will Make You Happy Is Being Happy With Who You Are")
		pass

class PushButton(Button):
	pass

	def click(self):
		# print("Push Button Click")
		print("Life Is Like Riding Bicycle. To Keep Your Balance, You Must Keep Moving")

class RadioButton(Button):

	def click(self):
		# print("Radio Button Click")
		print("The Hard Days What Makes You Stronger")

button1 = PushButton()
# button2 = Button()
button3 = RadioButton()

button1.click()
# button2.click()
button3.click()

# help(button1)
