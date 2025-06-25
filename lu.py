#LAB 10 : To solve the system of linear equations using LU decomposition method

import numpy as np
import scipy.linalg as slg

n = int(input('No of variables: '))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Enter row {i+1} elements: ").split())))

print(f"The matrix A is:\n", np.matrix(A))

B = np.array(list(map(float, input('Enter the column terms: ').split())))
B = np.array(B)
print(f"The output matrix in B:\n", np.matrix(B))

P, L, U = slg.lu(A)
lum = slg.lu_factor(A)
print(f"The lower triangular matrix L is:\n", np.matrix(L))
print(f"The upper triangular matrix U is:\n", np.matrix(U))
print(f"The permutation matrix P is:\n", np.matrix(P))

X = slg.lu_solve(lum, B)
print(f"The solution vector X is:\n", np.matrix(X))