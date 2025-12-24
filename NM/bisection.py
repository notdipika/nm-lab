#To find a real root of a non-linear equation by bisection method using Python Programming

# import numpy as np

# eqn = input('Enter the equation in x using Python Syntax: ')
# def F(x, eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# a,b = float(input('Enter the first initial guess: ')), float(input('Enter the second guess: '))

# if f(a)*f(b)>0:
#     print(f'No root lies in the interval({a},{b})')

# else:
#     e,N=float(input('Enter the tolerable error: ')), int(input('Enter the maximum no of iterations: '))
#     itr=1
#     while itr<=N:
#         c=(a+b)/2
#         if f(a)*f(c)<0:
#             b=c
#         else:
#             a=c
#         error=abs(b-a)
#         if error<e:
#             print(f'The approximate root is {(a+b)/2} in {itr} iterations.')
#             break
#         itr+=1

#     if itr>N:
#         print(f'Solution does not converge in {N} iterations.')



# import numpy as np
# import pandas as pd

# eqn = input('Enter the equation in x using Python Syntax: ')
# def F(x, eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# a,b = float(input('Enter the first initial guess: ')), float(input('Enter the second guess: '))

# if f(a)*f(b)>0:
#     print(f'No root lies in the interval({a},{b})')

# else:
#     e,N=float(input('Enter the tolerable error: ')), int(input('Enter the maximum no of iterations: '))
#     itr=1
#     A=[]
#     while itr<=N:
#         c=(a+b)/2
#         A.append([itr, a, b, c, f(a), f(b), f(c)])
#         if f(a)*f(c)<0:
#             b=c
#         else:
#             a=c
#         error=abs(b-a)
#         if error<e:
#             A = pd.DataFrame(A, columns=['iterations','a','b','c','f(a)', 'f(b)', 'f(c)']). to_string(index=False)
#             print (A)
#             print(f'The approximate root is {c} in {itr} iterations.')
#             break
#         itr+=1

#     if itr>N:
#         print(f'Solution does not converge in {N} iterations.')


# import numpy as np
# import pandas as pd
# import matplotlib
# matplotlib.use('TkAgg')  
# import matplotlib.pyplot as plt
# import math

# eqn = input('Enter the equation in x using Python Syntax: ')
# def F(x, eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# a,b = float(input('Enter the first initial guess: ')), float(input('Enter the second guess: '))

# if f(a)*f(b)>0:
#     print(f'No root lies in the interval({a},{b})')

# else:
#     e,N=float(input('Enter the tolerable error: ')), int(input('Enter the maximum no of iterations: '))
#     itr=1
#     A=[]
#     m=[]
#     while itr<=N:
#         c=(a+b)/2
#         A.append([itr, a, b, c, f(a), f(b), f(c)])
#         m.append(c)
#         if f(a)*f(c)<0:
#             b=c
#         else:
#             a=c
#         error=abs(b-a)
#         if error<e:
#             A = pd.DataFrame(A, columns=['iterations','a','b','c','f(a)', 'f(b)', 'f(c)']).to_string(index=False)
#             print (A)
#             print(f'The approximate root is {(a+b)/2} in {itr} iterations.')
#             break
#         itr+=1

#     if itr>N:
#         print(f'Solution does not converge in {N} iterations.')

    
# m=np.array(m)
# x= np.linspace(-5,5,1000)
# plt.plot(x,f(x), label=eqn)
# plt.axhline(0,0, color='blue')
# plt.axvline(0,0, color='red')
# plt.grid(True)
# plt.title('Function Plot')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.scatter(m,f(m))
# for i, val in enumerate(m):
#     plt.text(val,f(val), f'{i+1}')
# plt.show()



import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

# User input for the equation
eqn = input('Enter the equation in x using Python syntax (e.g., math.sin(x) - x/2): ')

# Define the function safely
def F(x, eqn):
    return eval(eqn, {"x": x, "math": math, "np": np})

def f(x):
    return F(x, eqn)

# Get initial guesses
a = float(input('Enter the first initial guess (a): '))
b = float(input('Enter the second guess (b): '))

# Check if root is bracketed
if f(a) * f(b) > 0:
    print(f'No root lies in the interval ({a}, {b})')
else:
    e = float(input('Enter the tolerable error: '))
    N = int(input('Enter the maximum number of iterations: '))
    itr = 1
    rows = []
    
    while itr <= N:
        c = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fc = f(c)
        rows.append([itr, a, b, c, fa, fb, fc])
        
        if abs(fc) < e or abs(b - a) < e:
            break
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        itr += 1

    # Output the result table
    df = pd.DataFrame(rows, columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
    print('\nBisection Method Iterations:\n')
    print(df.to_string(index=False))
    print(f'\nThe approximate root is {(a + b) / 2:.6f} after {itr} iterations.')
    
    if itr > N:
        print(f'Solution did not converge in {N} iterations.')
