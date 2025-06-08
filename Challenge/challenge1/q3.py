'''Write a function to check if a number is an Armstrong number or not. The catch is that the number is provided in string format.
          Sample Input: “153”
          Sample Output: Armstrong Number
'''

def arms(value):
    a = len(value)
    temp = 0
    for i in range(a):
        temp += int(value[i])**a
    if (temp == int(value)):
        return True
    return False

if(arms("1555")):
    print("It is a armstrong Number")
else:
    print("Not a Armstrong Number")