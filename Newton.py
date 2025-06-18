#LAB-3: To find the real root of a non linear equation by Newton_Raphson Method using Python Programming

import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import pandas as pd

eqn = input("Enter the equation in x using the python syntax:\n")

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

def g(f, x, h=1e-10):
    return (f(x + h) - f(x - h)) / (2*h)

a = float(input("Enter the initial guess for the root:\n"))

if g(f, a) == 0:
    print("The derivative at the initial guess is zero. Please provide a different initial guess.")
else:
    e, N = float(input("Enter the error tolerance: ")), int(input("Enter the maximum number of iterations: "))
    itr = 1
    itr_table = []
    new_point = []

    while itr <= N:
        c = a - f(a) / g(f, a)
        error = abs(f(c))
        new_point.append(c)
        itr_table.append([itr, a, c, f(a), g(f, a), g(f,c), error])
        
        if error < e:
            itr_table = pd.DataFrame(itr_table, columns=['Iteration', 'a', 'c', 'f(a)', 'g(f,a)', 'g(f,b)','Error'])
            print(itr_table.to_string(index=False))
            print(f"The root is approximately {c} in {itr} iterations.")
            break
        
        a = c
        if g(f, a) == 0:
            print("The derivative at the initial guess is zero. Please provide a different initial guess.")
        else:
            itr += 1

x = np.linspace(-10, 10, 1000)
plt.plot(x, f(x), label=eqn, color='r')
plt.axhline(0, 0, color='blue')
plt.axvline(0, 0, color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Newton-Raphson Method')
plt.scatter(new_point, f(np.array(new_point)), color='green', label='Root Approximations')
for i, val in enumerate(new_point):
    plt.text(val, f(val), f"{i+1}")
plt.show()






































































# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# # np.exp(x)-np.sin(x)-9
# eqn = input("Enter the equation in x using the python syntax:\n")

# def F(x,eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# # derivative of f(x)
# def g(f,x,h=1e-10):
#     return ((f(x+h)-f(x))/h)

# print("Enter the initial guess for the root:\n")
# a = float(input("a: "))

# if g(f,a)== 0:
#     print("The derivative at the initial guess is zero. Please provide a different initial guess.")
# else:
#     e, N = float(input("Enter the error tolerance: ")), int(input("Enter the maximum number of iterations: "))
#     itr = 1
#     itr_table = []
#     new_point = []

#     while itr <= N:
#         c = a - f(a) / g(f, a)
#         error = abs(c - a)
#         new_point.append(c)
#         itr_table.append([itr, a, c, f(a),g(f,a), error])
        
#         if error < e:
#             itr_table = pd.DataFrame(itr_table, columns=['Iteration', 'a', 'c', 'f(a)','g(f,a)','Error'])
#             print(itr_table.to_string(index=False))
#             print(f"The root is approximately {c} in {itr} iterations.")
#             break
        
#         a = c
#         itr += 1
# x = np.linspace(-5, 5, 1000)
# plt.plot(x, f(x), label=eqn, color='r')
# plt.axhline(0, 0, color='blue')
# plt.axvline(0, 0, color='blue')
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('Newton-Raphson Method')
# plt.scatter(new_point, f(np.array(new_point)), color='green', label='Root Approximations')
# for i, val in enumerate(new_point):
#     plt.text(val, f(val), f"{i+1}")
# plt.show()
