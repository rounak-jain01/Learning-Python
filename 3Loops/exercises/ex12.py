'''Seprate each digit of a number and print it on the new line'''
num = int(input("Enter a Number: "))
ans = 0
sum = 0
while num != 0:
    ans = num % 10
    sum = sum+ans
    print(ans)
    num //=10


print(sum)
