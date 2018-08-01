varA = input("enter first number")
varB = input("enter second number")
x = type(varA)
y = type(varB)
if x == "str" or y == "str":
	print("string involved")
elif varA > varB:
	print("bigger")
elif varA == varB:
	print("equal")
else:
	print("smaller")
