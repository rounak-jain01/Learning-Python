#  Write a function that counts the frequency of elements in a list and removes the element(s) that occur the most number of times. Sample Input: - L = [1,1,2,4,5,6,6,5,4,3,2,2,3,4,6] Sample Output: - [1,1,2,4,5,5,4,3,3,2,2,3,4] 


def remove(numbers):
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] = counts[n] + 1
        else:
            counts[n] = 1
    
    highest = 0
    for n in counts:
        if counts[n] > highest:
            highest = counts[n]
    
    rmv = None
    for n in counts:
        if counts[n] == highest:
            if to_remove is None or n > to_remove:
                to_remove = n
    
    result = []
    for n in numbers:
        if n != to_remove:
            result.append(n)
    
    return result

l = [1,1,2,4,5,6,6,5,4,3,2,2,3,4,6]
ans = remove(l)
print(ans)
