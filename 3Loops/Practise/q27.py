'''Print all Prime numbers between 1 to *n*.'''

def printPrime(n1):
    for i in range(2,n1+1):
        for j in range(2,(i//2) + 1):
            if (i % j == 0):
                break
        else:
            print(i)

printPrime(25)

