'''Write a function which will check that is a number is prime or not.
          Sample Input: 12
          Sample Output: Prime
'''

def isPrime(num):
    if num <= 1:
        return "Neither Prime Nor Coprime"
    if num in (2,3):
        return "Prime Number"
    for i in range(2,(num//2)+1):
        if (num % i == 0):
            return "Not a Prime Number"
        return "Prime Number"
    
ans = isPrime(13)
print(ans)