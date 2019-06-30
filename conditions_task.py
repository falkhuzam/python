first_number=input("Enter first number:")
second_number=input("Enter second number:")
Operation=input("Enter Operation:")


if first_number.isnumeric() and second_number.isnumeric():
	if Operation == "+":
		print (int(first_number) + int(second_number))
	elif Operation == "-":
		print (int(first_number) - int(second_number))
	elif Operation == "*":
		print (int(first_number) * int(second_number))
	elif Operation == "/":
		print(int(first_number) / int(second_number))
	else:
		print ("The operation is not valid")
else:
	print ("Numbers were invalid")

