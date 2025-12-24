import math

# Allow user to input g(x) in terms of x
equation = input("Enter the equation in the form x = g(x), using Python syntax (e.g., cos(x), (1 + x)**0.5, etc.):\ng(x) = ")

# Define g(x) dynamically using eval
def g(x):
    return eval(equation)

# Initial guess, tolerance, and maximum iterations
x0 = float(input("Enter initial guess: "))
tolerance = float(input("Enter tolerance (e.g., 1e-6): "))
max_iterations = int(input("Enter maximum number of iterations: "))

print("\nFixed Point Iteration Method")
print("Iteration\t  x")

for i in range(1, max_iterations + 1):
    try:
        x1 = g(x0)
    except Exception as e:
        print(f"Error in evaluating g(x): {e}")
        break

    print(f"{i}\t\t  {x1:.6f}")

    if abs(x1 - x0) < tolerance:
        print(f"\nConverged to root: {x1:.6f} after {i} iterations")
        break

    x0 = x1
else:
    print("\nDid not converge within the maximum number of iterations.")
