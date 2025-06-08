'''Accept a number and check if it a perfect number or not.
      A number whose sum of factors(excluding number itself)  = Number 
      Ex -  6 = 1, 2, 3 = 6
'''

num = int(input("Enter a number to check if it is perfect or Not: "))
sum = 0

for i in range(1,num):
    if(num % i == 0):
        sum += i
    
if(num == sum):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a perfect Number")