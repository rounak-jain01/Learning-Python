'''24. Find the HCF (GCD) of two numbers. '''

def gcd(num1,num2):
    while num2 != 0:
        num1,num2 = num2,num1%num2
    return num1

ans = gcd(18,48)
print(ans),
        
