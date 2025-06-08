'''Check whether a number is a Prime number or not'''

def isprime(num):
    if num <= 1:  
        return f"{num} is neither prime nor composite"
    if num in (2, 3): 
        return f"{num} is a Prime Number"
    

    for i in range(2,(num//2)+1):
        if num % i == 0:
            return f"{num} is a Composite Number"
    return f"{num} is a Prime Number"
    
ans = isprime(4)
print(ans)