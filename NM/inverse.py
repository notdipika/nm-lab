# To find the smallest eigenvalue and corresponding eigenvector of a square matrix using Inverse Power Method
import numpy as np
import pandas as pd
import sys

n = int(input("Enter the order of square matrix: "))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row: ").split())))
A = np.array(A)
print("The matrix A is:\n", np.matrix(A))
try:
    B = np.linalg.inv(A)
except np.linalg.LinAlgError:
    print("The matrix is singular and cannot be inverted.")
    sys.exit()

x = np.array(list(map(float, input("Enter the initial vector: ").split())))
e, N = float(input("Enter the tolerable error: ")), int(input("Enter the max no. of iterations: "))
itr = 1
T = []
oldev = 0

while itr <= N:
    y = np.dot(B, x)
    maxev = abs(max(y, key=abs))
    x = y / maxev 
    T.append([itr, (1/maxev)]+ x.tolist())
    err = abs(maxev - oldev)
    if err < e:
        break
    oldev = maxev
    itr += 1

if itr > N:
    print(f"No smallest eigenvalue found in {N} iterations.")
else:
    print("The solution is:")
    print("Approximate eigenvector:\n", x)
    print(f"Smallest eigenvalue ≈ {1 / maxev:.6f}")
    T = pd.DataFrame(T, columns=['Iteration', 'Max Eigenvalue (1/λ)'] + [f'x{i+1}' for i in range(n)])
    print(T.to_string(index=False))