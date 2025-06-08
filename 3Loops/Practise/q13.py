n = int(input("Tell a Number: "))
fd = 0
ld = n % 10
while(n != 0):
    fd = n
    n //= 10

print("Before Swapping")
print(f"First Digit {fd} \nLast Digit {ld}")
temp = fd
fd = ld
ld = temp
print("After Swapping")
print(f"First Digit {fd} \nLast Digit {ld}")