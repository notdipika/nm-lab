import numpy as np
import pandas as pd

n= int(input("No of rows: "))
A=[]

for i in range(n):
    A.append(list(map(float,input().split())))

A = np.matrix(A)
print(f"The augmented matrix A: \n {A}")

# Initial guess
X=[]
print("Enter the initial guess: ")
for i in range(n):
    X.append(list(map(float,input().split())))

X =np.matrix(X)
print(f"Inital Guess are: \n {X}")

e,N = float(input("Enter the tolerable error: ")), int(input("Enter the maximum number of iternation: "))
iteration = 0
itr_table =[]

while iteration<=N:
    X_old = np.copy(X)
    for i in range(n):
        s = 0
        for j in range(n):
            if j!=i:
                s+=A[i,j]*X[j]
        X[i]=(A[i,-1]-s)/(A[i,i])
    X= np.array(X)
    itr_table.append([iteration]+[X[i,0] for i in range(n)])
    err = np.abs(X-X_old)
    if np.all(err<e):
        break
    iteration+=1

if iteration>N:
    print(f"The solution not found in {N} iteration")
else:
    print("The solution is: ")
    itr_table = pd.DataFrame(itr_table,columns=['iteration']+[f"x{i+1}" for i in range(n)])
    print(itr_table)
    for i in range(n):
        print(f"X{i+1}={X[i]}")