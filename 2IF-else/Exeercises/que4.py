'''Accept an integer and check whether it is an even number or odd.'''
num = int(input("Enter a number to check whether it is odd or even: "))

if(num % 2 == 0):
    print("Given Number",num, "is Even")
else:
    print("Given Number",num, "is Odd")
