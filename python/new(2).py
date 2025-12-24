# from module import *
# from module import simpleInterest, compoundINterest
import module
p = float(input("Enter principal amount: "))
t = float(input("Enter time in years: "))
r = float(input("Enter rate of interest: "))
print(f'Simple Interest is {module.simpleInterest(p,t,r):.3f}')
print(f'Compound Interest is {module.compoundINterest(p,t,r):.3f}')
