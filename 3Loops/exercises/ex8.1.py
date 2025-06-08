s = int(input("Starting Point "))
e = int(input("Ending Point "))

for i in range(s, e+1):
    if (i % 7 == 0) or (10 % i == 0):
        print(i)