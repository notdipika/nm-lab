import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import math

# Input function
eqn = input('Enter the equation in x using Python Syntax: ')

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

# Initial guesses
a, b = float(input('Enter the first initial guess: ')), float(input('Enter the second guess: '))

if f(a) * f(b) > 0:
    print(f'No root lies in the interval ({a}, {b})')
else:
    e = float(input('Enter the tolerable error: '))
    N = int(input('Enter the maximum number of iterations: '))
    
    itr = 1
    A = []
    m = []
    
    while itr <= N:
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)  # Regula Falsi formula
        fc = f(c)
        A.append([itr, a, b, c, fa, fb, fc])
        m.append(c)
        
        if abs(fc) < e:
            break
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        if abs(b - a) < e:
            break
        
        itr += 1

    # Display results
    df = pd.DataFrame(A, columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
    print(df.to_string(index=False))

    if itr <= N:
        print(f'\nThe approximate root is {c} found in {itr} iterations.')
    else:
        print(f'\nSolution did not converge in {N} iterations.')

    # Plotting the function and iterations
    m = np.array(m)
    x = np.linspace(-1,5,1000)
    plt.plot(x, f(x), label=f'f(x) = {eqn}')
    plt.axhline(0, color='blue')
    plt.axvline(0, color='red')
    plt.grid(True)
    plt.title('Regula Falsi Method: Function Plot')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.scatter(m, f(m), color='green')
    for i, val in enumerate(m):
        plt.text(val, f(val), f'{i+1}')
    plt.show()
