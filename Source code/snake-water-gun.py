import random
print("Snake water gun")
options=["s","w","g"]				
print("\nSnake - s\nWater - w\nGun - g\n")
userch=input("Enter your choice : ")
if userch in options:
	compch=random.choice(options)
	if compch=="s":
		if userch=="w":
			print("Computer won")
		else:
			print("You won")
	elif compch=="w":
		if userch=="g":
			print("Computer won")
		else:
			print("You won") 
	else:
		if userch=="s":
			print("Computer won")
		else:
			print("You won")	
else:
	print("Select correct option next time")
	exit()
