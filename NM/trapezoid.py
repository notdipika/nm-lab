#To evaluate finite integral using trapezoidal rule

import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter lower limit: '))
b = float(input('Enter upper limit: '))
n = int(input('Enter number of subintervals: '))
h = (b - a) / n

func = input('Enter the integrand function in terms of x using python syntax: ')

def f(x, func):
    return eval(func)

def y(x):
    return f(x, func)

x = np.linspace(a, b, n + 1)
I = 0
s = 0

for i in range(1,n):
    s += y(x[i])

I = (h / 2) * (y(x[0]) + 2 * s + y(x[n]))
print(f'The approximate integral value from {a} to {b} is: {I}')

plt.plot(x, [y(x) for x in x], color = 'midnightblue', label='Integrand Function')
x_values = np.linspace(a - 10, b + 10, 1000)
plt.plot(x_values, [y(x) for x in x_values], color='powderblue', label='Fitted Curve')
y_values = [y(x) for x in x]
for i in range (n):
    xs = [x[i], x[i], x[i + 1], x[i + 1]]
    ys = [0, y_values[i], y_values[i + 1], 0]
    plt.fill(xs, ys, color='lightblue', alpha=0.5, edgecolor='blue', linewidth=1)
plt.title('Trapezoidal Rule Integration')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()