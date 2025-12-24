# LAB 11: To find Lagrange interpolation polynomial for the given data

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = int(input('Enter no of data: '))
X = np.array(list(map(float, input('Enter all x-data: ').split())))
Y = np.array(list(map(float, input('Enter all y-data: ').split())))
xp = float(input('Enter the point to interpolate: '))

x = sp.symbols('x')
poly = 0

for i in range(n):
    lf = 1
    for j in range(n):
        if (j != i):
            lf *= (x - X[j])/(X[i] - X[j])
    poly += Y[i] * lf
poly = sp.simplify(poly)

print ('The Lagrange Polynomial is: \n', poly)

int_val = poly.subs(x, xp)
print(f'The interpolated value at x = {xp} is {int_val}')


f = sp.lambdify(x, poly, 'numpy')

x_val = np.linspace(min(X)- 2, max(X) + 2, 1000)
plt.plot(x_val, f(x_val), label=poly, color='r')
plt.axhline(0, 0, color='blue')
plt.axvline(0, 0, color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Lagrange Polynomial')
plt.scatter(X, f(X), color="blue")
for i, val in enumerate(X):
    plt.text(val, f(val), f'{val}')
plt.scatter(xp, f(xp), color='green', label='Interpolated Point')
plt.show()






        
