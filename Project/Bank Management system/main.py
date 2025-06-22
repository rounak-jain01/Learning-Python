from pathlib import Path
import json
import random 
import string


class Bank:
    __database = "data.json"
    data = []

    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.loads(fs.read())

    except Exception as err:
        print(f"Error Occured as {err}")

    @classmethod
    def update_data(cls):
        with open(cls.__database, 'w') as fs:
            json.dump(cls.data,fs)

    @classmethod
    def generateAcc(cls):
        alpha = random.choices(string.ascii_letters,k=4)
        digits = random.choices(string.digits,k=8)
        id = alpha+digits
        random.shuffle(id)
        return "".join(id)


    def createuser(self):
        info = {
            "name": input("Enter your name: "),
            "email": input("Enter your email: "),
            "age": int(input("Enter your age: ")),
            "phonenumber": input("Enter your phone number: "),
            "AccountNo.": bank.generateAcc(),
            "pin": input("Enter your pin: "),
            "balance": 0
        }

        if info["age"] < 18:
            print("Your account cannot be created. You are not balik...")

        if len(info["phonenumber"]) != 10 or len(info["pin"]) != 4:
            print("Invalid input. Please try again later...")


        print(f"Please keep your account number safe: {info['AccountNo.']}")
        Bank.data.append(info)
        Bank.update_data()


    def depositMoney(self):
        acc = input("Please Enter Your Account Number ")
        pin = input("Please Enter Your Pin ")
        # for i in Bank.data:
        #     if i["AccountNo."] == acc and i["pin"] == pin:
        #         userdata = i
        #         print(userdata)
        #         break

        userdata = [i for i in Bank.data if i["AccountNo."] == acc and i["pin"]== pin]
        if userdata == False:
            print("No data Found for this User ")
        else:
            amt = int(input("Enter Your Amount "))
            if (amt <= 0):
                print("Please Input a Valid Amount ")
            elif amt > 10000:
                print("Amount is Greater than 10000")
            else:
                userdata[0]["balance"] += amt
                Bank.update_data()
                print("Money Deposited Successfully")


bank = Bank()
check = int(input("""
Press 1 to create a bank account: 
Press 2 For deposit Money
"""))

if check == 1:
    bank.createuser()

if check == 2:
    bank.depositMoney()