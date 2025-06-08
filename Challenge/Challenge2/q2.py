#  Write a function that rotates a list k times to the right. Sample Input: - k = 2, L = [10,20,30,40,50] Sample Output: - [30,40,50,10,20] 


def rotate_array(arr, k):
    
    for i in range(k):
        last = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = last
    
    return arr


arr =  [10,20,30,40,50] 
k = 2
rotated = rotate_array(arr, k)
print(rotated)



