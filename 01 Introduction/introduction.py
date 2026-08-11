class Food: # template
	pass

food1 = Food() # object / instance
food2 = Food()
food3 = Food()

food1.name = "Bubur Gurih"
food1.health = 100
food1.spicyLevel = 10

food2.name = "Bubur Kacang"
food2.health = 200
food2.spicyLevel = 20

food3.name = "Bubur Pecel"
food3.health = 500
food3.spicyLevel = 30

print(food1)
print(food1.__dict__)
print(food1.name)
