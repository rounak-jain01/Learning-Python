import random

a=random.randint(1,100)
count = 0
while True:
    guess = int(input("Please guess the number between 1 - 100: "))
    count +=1
    if guess == a:
        print("Congratulaion you found your number: ")
        print(f"You take {count} Number of trials to guess the number: {a}")
        break
    elif guess > a:
        print("Wrong go a little lower!!")
    elif guess < a :
        print("Go a Little Higher")
    

