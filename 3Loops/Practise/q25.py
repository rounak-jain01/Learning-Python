'''Find the LCM of two numbers.'''

def hcf(num1,num2):
    while num2 != 0:
        num1, num2 = num2,num1%num2
    return num1

def lcm(num1,num2):
    return ((num1*num2)//hcf(num1,num2))


ans = lcm(21,28)
print(ans)
