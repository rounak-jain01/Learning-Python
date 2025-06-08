n = int(input("Tell a Number: "))
count = 0
cpy = n
while(cpy != 0):
    count+=1
    cpy //= 10

print(f"{n} has {count} digits")