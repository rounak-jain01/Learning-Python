# Write a function that prints all the prime numbers between 100 and 400. Sample Output: - [101, 103, 107, 109, 113, ..., 397] 

def primes(start, end):
    primes = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
    return primes

ans = primes(100, 400)
print(ans)
