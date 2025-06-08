'''Calculate the factorial of a number.'''

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

ans = factorial(5)
print(ans)