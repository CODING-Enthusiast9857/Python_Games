import random
print("Snake water gun")
options=["s","w","g"]				
print("\nSnake - s\nWater - w\nGun - g\n")

while True:
	userch=input("\nEnter your choice : ")
	compch=random.choice(options)
	print("\nComputer choose ",compch,", User choose ",userch,"\n")
	
	if userch==compch:
		print(f"Both choose {compch}, It's Tie!!")
	elif userch=='s':
		if compch=='w':
			print("Snake drinks water! You won.")
		else:
			print("Gun kills snake! You lose.")
	elif userch=='w':
		if compch=='g':
			print("Gun drowned water! You won.")
		else:
			print("Snake drinks water! You lose.")
	elif userch=='g':
		if compch=='s':
			print("Gun kills snake! You won.")
		else:
			print("Gun drowned water! You lose.")
	elif userch not in options:
		print("Incorrect Choice! Please Choose from given options next time.")

	con=input("Play Again(y/n) --> ")
	if con.lower()!='y':
		break