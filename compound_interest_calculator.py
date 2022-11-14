print("***** Compound Interest Calculator *****\n")

principle=float(input("Enter principal amount : "))
rate=float(input("Enter rate of interest : "))
year=int(input("Enter no. of years : "))

compound_interest=principle*pow((1+rate/100),year)
print("Compound Interest : %.2f"%compound_interest)