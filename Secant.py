#LAB-2: To find the real root of a non-linear equation by Secant Method using Python Programming

# import numpy as np
# import pandas as pd
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

# eqn = input("Enter the equation in x using the python syntax:\n")

# def F(x, eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# a,b = float(input("Enter the first initial guess: ")), float(input("Enter the second initial guess: "))

# if f(a)==f(b):
#     print("The value becomes infinite at the initial guesses. Please provide different initial guesses.")

# else:
#     e, N = float(input("Enter the error tolerance: ")), int(input("Enter the maximum number of iterations: "))
#     itr = 1
#     itr_table = []
#     new_point = []

#     while itr <= N:
#         c = (a * f(b) - b * f(a)) / (f(b) - f(a))
#         error = abs(f(c))
#         new_point.append(c)
#         itr_table.append([itr, a, b, c, f(a), f(b), f(c), error])
        
#         if error < e:
#             itr_table = pd.DataFrame(itr_table, columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'Error'])
#             print(itr_table.to_string(index=False))
#             print(f"The root is approximately {c} in {itr} iterations.")
#             break
        
#         a, b = b, c
#         if f(a)==f(b):
#             print("The value becomes infinite at the initial guesses. Please provide different initial guesses.")
#         else:
#             itr += 1

# x = np.linspace(-10,10, 1000)
# plt.plot(x,f(x),label=eqn,color='r')
# plt.axhline(0,0,color='blue')
# plt.axvline(0,0,color='blue')
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('Secant Method')
# plt.scatter(new_point, f(np.array(new_point)), color='green', label='Root Approximations')
# for i, val in enumerate(new_point):
#     plt.text(val,f(val),f"{i+1}")
# plt.show()




























































import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

eqn = input("Enter the equation in x using the python syntax:\n")

def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

print("Enter the initial guesses for the root:\n")
a,b=float(input("a: ")), float(input("b: "))

if f(a)==f(b):
    print("The function values at the initial guesses are equal. Please provide different initial guesses.")

else:
    e,N = float(input("Enter the error tolerance: ")), int(input("Enter the maximum number of iterations: "))
    itr = 1
    itr_table=[]
    new_point = []

    while itr <= N:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        error =abs(c-b)
        new_point.append(c)
        itr_table.append([itr, a, b, c,f(a),f(b), f(c), error])
        if error < e:
            itr_table = pd.DataFrame(itr_table, columns=['Iteration', 'a', 'b', 'c','f(a)','f(b)', 'f(c)', 'Error'])
            print(itr_table.to_string(index=False))
            print(f"The root is approximately {c} in {itr} iterations.")
            break
        a, b = b, c
        itr += 1

x = np.linspace(-5,5, 1000)
plt.plot(x,f(x),label=eqn,color='r')
plt.axhline(0,0,color='blue')
plt.axvline(0,0,color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Secant Method')
plt.scatter(new_point, f(np.array(new_point)), color='green', label='Root Approximations')
for i, val in enumerate(new_point):
    plt.text(val,f(val),f"{i+1}")
plt.show()







# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# eqn = input("Enter the equation in x using the python syntax:\n")

# def F(x,eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# print("Enter the initial guesses for the root:\n")
# a,b=float(input("a: ")), float(input("b: "))

# if f(a)==f(b):
#     print("The function values at the initial guesses are equal. Please provide different initial guesses.")

# else:
#     e,N = float(input("Enter the error tolerance: ")), int(input("Enter the maximum number of iterations: "))
#     itr = 1
#     itr_table=[]
#     new_point = []

#     while itr <= N:
#         c = (a*f(b)-b*f(a))/(f(b)-f(a))
#         error =abs(c-b)
#         new_point.append(c)
#         itr_table.append([itr, a, b, c,f(a),f(b), f(c), error])
#         if error < e:
#             itr_table = pd.DataFrame(itr_table, columns=['Iteration', 'a', 'b', 'c','f(a)','f(b)', 'f(c)', 'Error'])
#             print(itr_table.to_string(index=False))
#             print(f"The root is approximately {c} in {itr} iterations.")
#             break
#         a, b = b, c
#         itr += 1

# x = np.linspace(-5,5, 1000)
# plt.plot(x,f(x),label=eqn,color='r')
# plt.axhline(0,0,color='blue')
# plt.axvline(0,0,color='blue')
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('Secant Method')
# plt.scatter(new_point, f(np.array(new_point)), color='green', label='Root Approximations')
# for i, val in enumerate(new_point):
#     plt.text(val,f(val),f"{i+1}")
# plt.show()