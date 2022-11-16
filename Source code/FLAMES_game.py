def flames(n1,n2):
	con=n1+n2
	
	for i in con:
		if con.count(i)!=1:
			con=con.replace(i,'')
		
	n=len(con)%6
	
	if n==1:
	   return "Friends"
	elif n==2:
	   return "Love"
	elif n==3:
	   return "Affection"
	elif n==4:
	   return "Marriage"
	elif n==5:
	   return "Enemy"
	elif n==6:
	   return "Siblings"
    	
n1=input("Enter 1st name : ")
n2=input("Enter 2nd name : ")
print("\nFLAMES : \nF - Friends\nL - Love\nA - Affection\nM - Marriage\nE - Enemy\nS - Siblings\n")
print("Relationship status is :",flames(n1,n2))
