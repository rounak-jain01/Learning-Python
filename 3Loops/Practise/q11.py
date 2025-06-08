n = int(input("Tell a Number: "))
ld = n % 10
fd = 0
while(n != 0):
    fd = n
    n //= 10
print(f"First Digit of the number is {fd}")
print(f"Last digit of the Number is {ld}")
