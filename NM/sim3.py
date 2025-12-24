#integration using simpsons 3/8 rule
import numpy as np
import matplotlib.pyplot as plt

a,b=float(input("enter the lower and upper value :")),float(input())
n=int(input("enter the number of sub intervals :"))
h=(b-a)/n
x=np.linspace(a,b,n+1)
func=input("enter the integrand function in python syntax :")
def F(x,func):
    return eval(func)
def y(x):
    return F(x,func)
y_points=[y(x) for x in x]
integral=0
s1=0
s2=0
for i in range(1,n):
    if i%3==0:
        s2+=y(x[i])
    else:
        s1+=y(x[i])
integral=3*(h/8)*(y(x[0])+3*s1+2*s2+y(x[n]))
print("The approximate integra value is ",integral)

plt.plot(x,y_points,label='Partation points',marker='x')
xval=np.linspace(a-10,b+10,1000)
plt.plot(xval,[y(x) for x in xval],label='Integrand Function')
for i in range(0,n,3):
    x_list=x[i:i+4]
    y_list=y_points[i:i+4]
    plt.fill_between(x_list,y_list,color='pink',alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simpson 3/8 Rule')
plt.legend()
plt.grid()
plt.show()
