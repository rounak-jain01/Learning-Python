'''Accept name and age from the user. Check if the user is a valid voter or not.
      Vaid - Hello Shery, You are a valid voter.
      Invalid - Sorry Shery, you can't cast the vote.
	Part 2 - Print after how many years the user will be eligible'''

name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))

if(age >= 18):
    print("Hello",name,"You are a Valid Voter" )
else:
    print("Sorry",name,"You can't cast the vote")
    print("You can cast the vote after",(18-age), "Years")
