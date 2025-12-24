# To solve the system of linear equations using Gauss Elimination Method with partial pivoting

import numpy as np

n = int(input('Enter the number of equations: '))
print('Enter the augmented matrix:')

A=[]

for i in range(n):
    A.append(list(map(float, input(f'Enter {i+1}th row: ').split())))

A = np.array(A)
print('The augmented matrix is:\n', A)

for i in range(n):
    P_row = np.argmax(abs(A[i:, i])) + i
    A[[i, P_row]] = A[[P_row, i]]  
    for j in range(i + 1, n):
        A[j] = A[j] - A[j, i]  * A[i] / A[i, i]

print('Upper triangular matrix after step:\n')
print(np.matrix(A))

x= np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (A[i, -1] - np.sum(A[i, i + 1:n] * x[i + 1:n])) / A[i, i]

print('The solution is:\n')

for i in range(n):
    print(f'x{i+1} = {x[i]}')


