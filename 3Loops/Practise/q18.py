n = int(input("Tell a Number: "))
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c0  = 0
while(n != 0):
    temp = n % 10
    match temp:
        case 1:
            c1+=1
        case 2:
            c2+=1
        case 3:
            c3+=1
        case 4:
            c4+=1
        case 5:
            c5+=1
        case 6:
            c6+=1
        case 7:
            c7+=1
        case 8:
            c8+=1
        case 9:
            c9+=1
        case 0:
            c0+=1
    n //= 10


print("Frequency of 1",c1)
print("Frequency of 2",c2)
print("Frequency of 3",c3)
print("Frequency of 4",c4)
print("Frequency of 5",c5)
print("Frequency of 6",c6)
print("Frequency of 7",c7)
print("Frequency of 8",c8)
print("Frequency of 9",c9)
print("Frequency of 0",c0)
