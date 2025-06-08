'''Find all factors of a number.'''

def factor(num):
    for i in range(1,(num//2)+1):
        if num % i == 0:
            print(i)

factor(15)