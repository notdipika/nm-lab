# #LAB 9: To find the dominant eigen values and corresponding eigen vectors of a square matrix using inverse method

# import numpy as np
# import pandas as pd

# n= int (input('Enter the order of the matrix: '))
# A=[]
# for i in range (n):
#     A.append(list(map(float, input(f"Enter row {i+1} elements: ").split())))

# A = np.array(A)
# print (f"The matrix A is:\n", np.matrix(A))

# x = np.array(list(map(float, input('Enter the initial vector: ').split())))
# x = np.array(x)

# def inv(A):
#     try:
#         return np.linalg.inv(A)
#     except:
#         print("Matrix is singular, cannot compute inverse.")

# B = np.matrix(inv(A))

# e,N = float(input("Enter the tolerable error: ")), int(input("Enter the maximum number of iterations: "))

# itr = 1
# oldev = 0
# itr_table = []

# while itr <= N:
#     y = np.dot(B, x)
#     maxev = abs(max(y, key=abs))
#     x = y / maxev
#     itr_table.append([itr, maxev])
#     error = abs(maxev - oldev)
#     if error < e:
#         break
#     oldev = maxev
#     itr += 1

# if itr > N:
#     print(f'No dominant eigen value found in {N} iterations.')
# else:
#     print("The solution is: ")
#     itr_table = pd.DataFrame(itr_table, columns=['iteration', 'max_eigen_value']).to_string(index=False)
#     print(itr_table)
#     print(f'The dominant eigen value is: {maxev} in {itr} iterations.')
#     print(f'The corresponding eigen vector is:\n', np.matrix(x))


# LAB 9: To find the dominant eigen values and corresponding eigen vectors using inverse method

import numpy as np
import pandas as pd

n = int(input('Enter the order of the matrix: '))
A = []

for i in range(n):
    A.append(list(map(float, input(f"Enter row {i+1} elements: ").split())))

A = np.array(A)
print(f"\nThe matrix A is:\n{np.matrix(A)}")

x = np.array(list(map(float, input('\nEnter the initial vector: ').split())))

def inv(A):
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        print("Matrix is singular, cannot compute inverse.")
        exit()

B = np.matrix(inv(A))

e = float(input("\nEnter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))

itr = 1
oldev = 0
itr_table = []

while itr <= N:
    y = np.dot(B, x)
    maxev = max(abs(y))  # Dominant eigenvalue (reciprocal)
    x = y / maxev        # Normalize vector

    itr_table.append([itr, maxev])
    error = abs(maxev - oldev)

    if error < e:
        break

    oldev = maxev
    itr += 1

if itr > N:
    print(f'\nNo dominant eigen value found in {N} iterations.')
else:
    print("\nThe solution is:")
    print(pd.DataFrame(itr_table, columns=['Iteration', 'Eigen Value']).to_string(index=False))
    print(f'\nThe dominant eigen value is: {1/maxev:.6f} (approx) in {itr} iterations.')
    print(f'\nThe corresponding eigen vector is:\n{np.matrix(x)}')
