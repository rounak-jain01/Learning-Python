'''Print Fibonacci series up to *n* terms.'''

def fibbo(n):
    n1 = 0
    n2 = 1
    for i in range(0,n):
        print(n1)
        n1,n2 = n2,n1+n2

fibbo(8)