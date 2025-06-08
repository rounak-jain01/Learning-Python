'''Accept the parameters and calculate the Compound Interest & print it on STDOUT (Use Math class methods)'''
import math
ppl = int(input("Please Enter the Principle Amount: "))
roi = int(input("Please Enter the Rate of Interest: "))
time = int(input("Please Enter the Time Duration: "))

i = (1+(roi//100))
amt = ppl*math.pow(i,time)
ci = amt - ppl

print(ci)
