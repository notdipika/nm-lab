#LAB 16: To solve initial value problem of 1st order by using R-K-4 method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ode = input ('Enter dy/dx in terms of x and y using python syntax: ')

def F(x, y, ode):
    return eval(ode)

def f(x,y):
    return F(x, y, ode)

x = float(input('Enter the initial value of x: '))
y = float(input('Enter the initial value of y: '))
h = float(input('Enter the step size: '))
n = int(input('Enter the number of steps: '))

L = []
x_list = []
y_list = []

for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    
    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x += h
    L.append([x, y])
    x_list.append(x)
    y_list.append(y)

L = pd.DataFrame(L, columns=['x', 'y'])
print(L)

plt.plot(x_list, y_list, marker='x', label='RK4 Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Runge-Kutta 4th Order Method')
plt.legend()
plt.grid(True)
plt.show()