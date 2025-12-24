# To solve the system of linear equations using Gauss Jordan Method
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
    A[i] = A[i] / A[i, i]  
    for j in range(n):
        if j != i:
            A[j] = A[j] - A[j, i] * A[i]

print(f'The upper triangular matrix after step:\n')
print(np.matrix(A))

x = A[:, -1]
print('The solution is:\n', x)