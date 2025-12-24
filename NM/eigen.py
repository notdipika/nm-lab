#LAB 8: To find the dominant eigen values and corresponding eigen vectors of a square matrix using power method

import numpy as np
import pandas as pd

n= int (input('Enter the order of the matrix: '))
A=[]
for i in range (n):
    A.append(list(map(float, input(f"Enter row {i+1} elements: ").split())))

A = np.array(A)
print (f"The matrix A is:\n", np.matrix(A))

x = np.array(list(map(float, input('Enter the initial vector: ').split())))
x = np.array(x)

e,N = float(input("Enter the tolerable error: ")), int(input("Enter the maximum number of iterations: "))

itr = 1
oldev = 0
itr_table = []

while itr <= N:
    y = np.dot(A,x)
    maxev = abs(max(y, key=abs))
    for i in range (n):
        x = y/maxev
    itr_table.append([itr, maxev]+ [x[i] for i in range (n)])
    error = abs(maxev - oldev)
    if error < e:
        break
    oldev = maxev
    itr += 1


if itr > N:
    print(f'No dominant eigen value found in {N} iterations.')
else:
    print("The solution is: ")
    itr_table = pd.DataFrame(itr_table,columns=['iteration', 'max_eigen_value']+[f"x{i+1}" for i in range(n)]).to_string(index=False)
    print(itr_table)
    print(f'The dominant eigen value is: {maxev} in {itr} iterations.')
    print(f'The corresponding eigen vector is:\n', np.matrix(x))

