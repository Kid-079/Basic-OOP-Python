# Create Class Abstract

class Button():

	def click(self):
		# print("Button Click")
		# print("You Will Grow Beautifully In Your Own Way")
		print("The Only Thing Will Make You Happy Is Being Happy With Who You Are")

class PushButton(Button):

	def click(self):
		# print("Push Button Click")
		print("Life Is Like Riding Bicycle. To Keep Your Balance, You Must Keep Moving")

button1 = PushButton()
button1.click()