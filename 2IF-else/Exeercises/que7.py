'''Accept a year and check if it a leap year or not'''

year = int(input("Enter the Year: "))

if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print(year, "is the leap Year")
else:
    print(year, "Not a Leap Year")