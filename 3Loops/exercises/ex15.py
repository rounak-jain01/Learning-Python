'''Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
       Ex - 12321 - Rerverse - 12321
'''

num = int(input("Enter a Number: "))
result = num
n = 0
while num != 0:
    temp = num%10
    n = n*10 + temp
    num //= 10
if(result == n):
    print(result, "is a Palindrome Number")
else:
    print(result, "is not a Palindrome Number")