def simpleInterest(p,t,r):
    si = (p*t*r)/100
    return si
  
def compoundINterest(p,t,r):
    ci = p * ((1 + r / 100)** t) - p
    return ci
    
if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    t = float(input("Enter time in years: "))
    r = float(input("Enter rate of interest: "))
    print(f'Simple Interest is {simpleInterest(p,t,r):.3f}')
    print(f'Compound Interest is {compoundINterest(p,t,r):.3f}')
