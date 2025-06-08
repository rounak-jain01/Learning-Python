'''Take 3 int inputs from user and check and print the result.
	all are equal
	any of two are equal'''

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if((num1 == num2) and (num1 == num3) and (num2 == num3)):
    print("All Numbers are equal")
elif((num1 == num2) or (num1 == num3) or (num2 == num3)):
    print("Two Numbers are Equal")
else:
    print("No numbers are Equal")