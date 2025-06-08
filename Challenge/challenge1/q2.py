'''Write a one-liner function using ternary if-else to check whether a given year is a leap year or not.
           Sample Input: 2000
           Sample Output: Leap Year
'''
num = 2001
print("Leap Year" if ((num % 4 == 0) or (num % 400 == 0)) else "Not a Leap Year")
# print(ans)