'''Print all the factors of a number.'''

num = int(input("Please Enter a Number: "))

for i in range(1,num+1):
    if(num%i == 0):
        print(i, end=" ")
print("are the Factors of",num)


