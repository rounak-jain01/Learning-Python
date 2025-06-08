'''Find the Power of a number using for Loop'''

def power(num,exp):
    rslt = 1
    for i in range(exp):
        rslt *= num
    return rslt

ans = power(2,4)
print(ans)