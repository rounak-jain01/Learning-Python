'''Write a function that prints the Fibonacci series up to the number provided by the user.
          Sample Input: 5
          Sample Output: 0 1 1 2 3
'''

def fibbo(num):
    n1 = 0
    n2 = 1
    for i in range(1,num+1):
        print(n1,end=" ")
        n1,n2 = n2,n1+n2

fibbo(8)