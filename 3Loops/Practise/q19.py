n = int(input("Tell a Number: "))
cpy = n
rev = 0
while(n != 0):
    rev = (rev * 10) + (n % 10)
    n //= 10
print(rev)
while(rev != 0):
    temp = rev % 10
    match temp:
        case '0':
            print("zero", end=" ")
        case 1:
            print("one", end=" ")
        case 2:
            print("two", end=" ")
        case 3:
            print("three", end=" ")
        case 4:
            print("four", end=" ")
        case 5:
            print("five", end=" ")
        case 6:
            print("six", end=" ")
        case 7:
            print("seven", end=" ")
        case 8:
            print("eight", end=" ")
        case 9:
            print("nine", end=" ")
    rev //= 10