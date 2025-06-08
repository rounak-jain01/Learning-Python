'''Stack Memory Implementation'''

def hello1():
    hello2()
    print("Hello 1")

def hello2():
    hello3()
    print("Hello 2")

def hello3():
    hello4()
    print("Hello 3")

def hello4():
    print("Hello 4")

hello1()

