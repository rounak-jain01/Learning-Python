'''Print all the numbers which are either divisible by 3 or 5 in a range'''

num = int(input("Enter a Number: "))

for i in range(1,num+1):
    if((i%3 == 0) or (i%5 == 0)):
        print(i,",", end=" ")
print("is divisible by either 3 or 5")