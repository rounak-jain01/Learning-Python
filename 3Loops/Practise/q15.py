n = int(input("Tell a Number: "))
prod = 1
while n != 0:
    prod *= (n %10)
    n //= 10
print(prod)