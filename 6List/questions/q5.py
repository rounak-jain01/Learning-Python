'''Accept size n from user and create a n size List then take n inputs into the and finally 
   Print the sum of all elements in the List in the following manner
   10 + 20 + 30 = 60'''
l = []
sum = 0
size = int(input("Enter the size of List: "))
for i in range(size):
    value = int(input("Enter Values: "))
    l.append(value)

for i in l:
    sum += i
    print(f"{i}+",end=" ")

print(f"= {sum}")
    