'''Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43'''

num = int(input("Please Enter a Number: "))
sum = 0
for i in range(1,num):
    if(num%i == 0):
        sum += i
        print(i, end=" ")
print("are the Factors of",num)
print("Sum of all the factors is",sum)