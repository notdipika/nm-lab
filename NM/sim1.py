#to evaluate integration from a to b f(x) using Simpson Rule
import numpy as np
import matplotlib.pyplot as plt

a=float(input('Enter the lower limit: '))
b=float(input('Enter the Upper limit: '))
n=int(input('Enter the no. of sub-intervals: '))

if n%2!=0:
    print('Number of sub-intervals must be Even! ')
    exit()
else:
    ode=input('Enter the integrand Function in terms of x: ')
    def F(x,ode):
        return eval(ode)
    def y(x):
        return F(x,ode)
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    y_points=[y(x) for x in x]
    s1=0
    s2=0
    for i in range(1,n):
        if i%2==1:
            s1+=y(x[i])
        else:
            s2+=y(x[i])
    I=(h/3)*(y(x[0])+4*s1+2*s2+y(x[n]))
    print(f'The integral by simphson 1/3 rule is {I} ')

    plt.plot(x,y_points,label='Partation points',marker='x')
    xval=np.linspace(a-10,b+10,1000)
    plt.plot(xval,[y(x) for x in xval],label='Integrand Function')
    for i in range(0,n,2):
        x_list=x[i:i+3]
        y_list=y_points[i:i+3]
        plt.fill_between(x_list,y_list,color='pink',alpha=0.2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simpson 1/3 Rule')
    plt.legend()
    plt.grid()
    plt.show()
