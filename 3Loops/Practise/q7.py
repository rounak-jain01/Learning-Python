n = int(input("Tell a Number: "))
sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum += i
print(f"Sum of All even number between 1 to {n} is {sum}")