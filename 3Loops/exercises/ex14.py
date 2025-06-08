'''Accept a number and print its reverse'''

num = int(input("Enter a Number: "))
temp = 0
n = 0
while num != 0:
    temp = num%10
    n = n*10 + temp
    num //= 10

print(n)