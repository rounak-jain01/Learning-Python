n = int(input("Tell a Number: "))
sum = 0
while n != 0:
    sum += n %10
    n //= 10
print(sum)