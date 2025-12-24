#LAB 16: To solve initial value problem of 1st order by using Heun's method

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
    y_predictor = y + h * f(x, y)
    y_corrector = y + (h / 2) * (f(x, y) + f(x + h, y_predictor))
    y = y_corrector
    x += h
    L.append([x, y])
    x_list.append(x)
    y_list.append(y)

L = pd.DataFrame(L, columns=['x', 'y'])
print(L)

plt.plot(x_list, y_list, marker='x', label='Heuns Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Heuns Method')
plt.legend()
plt.grid(True)
plt.show()