n = int(input("Tell a Number: "))
cpy = n
rev = 0
while(n != 0):
    temp = n % 10
    rev = (rev* 10) + temp
    n //= 10

if rev == cpy : print(f"{cpy} is a Palindrome Number")
else : print(f"{cpy} is not a Palindrome Number")