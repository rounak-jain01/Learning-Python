'''Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]'''

l = [2,3,15,15,3,2]

start = 0
end = len(l)-1

while(start < end):
    if l[start] != l[end]:
        print(f"List is not a Palindromic List")
        break;
    start += 1
    end -= 1
else:
    print(f"List is a Palindrome")
