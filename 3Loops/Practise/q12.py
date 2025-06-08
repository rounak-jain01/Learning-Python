n = int(input("Tell a Number: "))
ld = n % 10
fd = 0
while n != 0:
    fd = n
    n //= 10

sum = fd + ld
print(f"Sum of {fd} and {ld} is {sum}")