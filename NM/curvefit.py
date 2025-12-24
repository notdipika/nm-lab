#To fit second degree curve y = a + bx + cx^2 to the given data using least square method

import numpy as np
import matplotlib.pyplot as plt

x = np.array(list(map(float, input('Enter all x-data: ').split())))
y = np.array(list(map(float, input('Enter all y-data: ').split())))
n= len(x)

A = [[n, np.sum(x), np.sum(x**2)], 
     [np.sum(x), np.sum(x**2), np.sum(x**3)], 
     [np.sum(x**2), np.sum(x**3), np.sum(x**4)]]

B = [[np.sum(y)], [np.sum(x*y)], [np.sum(x**2*y)]]

print('The coefficient matrix of normal equation is:\n', np.matrix(A))
print('The constants of normal equation is: \n', np.matrix(B))

inv_A = np.linalg.inv(A)
coeff = np.dot(inv_A, B)
a = coeff[0]
b = coeff[1]
c = coeff[2]

print (f'The curve of best fit is: y = {a} + {b}x + {c}x^2')

X = np.linspace(min(x) - 10, max(x) + 10, 1000)
Y = a + b * X + c * X**2
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(X, Y, color='red', label='y = a + bx + cx^2')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve Fitting using Least Squares Method')
plt.legend()
plt.grid(True)
plt.show()


