'''Accept two numbers and print the greatest between them'''

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

if(num1>num2):
    print(num1, "is greater than", num2)
elif(num2>num1):
    print(num2, "is greater than", num1)
else:
    print("Both the Numbers are Equal")