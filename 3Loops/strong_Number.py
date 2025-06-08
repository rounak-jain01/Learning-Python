'''Checking given number is Strong or Not 
    ex- 1,2,145,40585
'''

num = int(input("Enter a number: "))
cpy = num
ans = 0
while(num != 0):
    temp = num % 10
    fact = 1
    for i in range(1,temp+1):
        fact *=i
    ans += fact
    num //= 10

if ans == cpy:
    print(f"{cpy} is a Strong Number")
else:
    print(f"{cpy} is Not a Strong Number")
