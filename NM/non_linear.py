import numpy as np

# Get user input for equations
print("Enter the system of equations in the form f(x,y) = 0 and g(x,y) = 0")
print("Use Python syntax with 'x' and 'y' as variables")
print("Available functions: np.sin, np.cos, np.tan, np.log, np.exp, np.sqrt, etc.")
print("\nExample: x**2 + y - 5 for f(x,y)")
print("Example: y**2 + x - 3 for g(x,y)")

f_eqn = input("\nEnter f(x,y): ")
g_eqn = input("Enter g(x,y): ")

# Define the system of equations using eval
def f(x, y):
    return eval(f_eqn, {"__builtins__": {}, "x": x, "y": y, "np": np})

def g(x, y):
    return eval(g_eqn, {"__builtins__": {}, "x": x, "y": y, "np": np})

# Numerical partial derivatives
def f1(x, y, h=1e-8):  # ∂f/∂x
    return (f(x + h, y) - f(x - h, y)) / (2 * h)

def f2(x, y, h=1e-8):  # ∂f/∂y
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

def g1(x, y, h=1e-8):  # ∂g/∂x
    return (g(x + h, y) - g(x - h, y)) / (2 * h)

def g2(x, y, h=1e-8):  # ∂g/∂y
    return (g(x, y + h) - g(x, y - h)) / (2 * h)

def newton_raphson_system(x0, y0, tol=1e-6, max_iter=100):
    x = x0
    y = y0

    print("\n--- Newton-Raphson Iteration ---")
    for i in range(max_iter):
        try:
            fx = f(x, y)
            gx = g(x, y)

            j11 = f1(x, y)
            j12 = f2(x, y)
            j21 = g1(x, y)
            j22 = g2(x, y)

            J = np.array([[j11, j12],
                          [j21, j22]])
            F = np.array([fx, gx])

            print(f"\nIteration {i+1}:")
            print(f"x = {x:.6f}, y = {y:.6f}")
            print(f"f(x, y) = {fx:.6f}, g(x, y) = {gx:.6f}")
            print(f"Jacobian: [[{j11:.6f}, {j12:.6f}], [{j21:.6f}, {j22:.6f}]]")

            # Check if Jacobian determinant is too small
            det_J = np.linalg.det(J)
            if abs(det_J) < 1e-12:
                print(f"Jacobian determinant is too small ({det_J:.2e}). Cannot continue.")
                return None, None

            delta = np.linalg.solve(J, F)
            dx, dy = delta
            print(f"Δx = {dx:.6f}, Δy = {dy:.6f}")

            x -= dx
            y -= dy

            print(f"New values: x = {x:.6f}, y = {y:.6f}")

            if abs(dx) < tol and abs(dy) < tol:
                print(f"\nConverged after {i+1} iterations!")
                return x, y

        except Exception as e:
            print(f"Error in iteration {i+1}: {e}")
            return None, None

    print(f"\nDid not converge within {max_iter} iterations.")
    return x, y

# --- Main Execution ---
try:
    print("\nEnter initial guesses:")
    x0 = float(input("Enter initial guess for x: "))
    y0 = float(input("Enter initial guess for y: "))
    
    # Optional: custom tolerance and max iterations
    use_defaults = input("\nUse default tolerance (1e-6) and max iterations (100)? (y/n): ").lower()
    if use_defaults == 'n':
        tol = float(input("Enter tolerance: "))
        max_iter = int(input("Enter maximum iterations: "))
    else:
        tol = 1e-6
        max_iter = 100
        
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

try:
    # Test the functions with initial values
    test_f = f(x0, y0)
    test_g = g(x0, y0)
    print(f"\nInitial function values:")
    print(f"f({x0}, {y0}) = {test_f}")
    print(f"g({x0}, {y0}) = {test_g}")
    
except Exception as e:
    print(f"Error evaluating functions: {e}")
    print("Please check your equation syntax.")
    exit()

result = newton_raphson_system(x0, y0, tol, max_iter)

if result[0] is not None:
    x_final, y_final = result
    print(f"\nFinal Solution: x = {x_final:.6f}, y = {y_final:.6f}")
    
    # Verification
    print(f"\nVerification:")
    try:
        f_final = f(x_final, y_final)
        g_final = g(x_final, y_final)
        print(f"f({x_final:.6f}, {y_final:.6f}) = {f_final:.8f}")
        print(f"g({x_final:.6f}, {y_final:.6f}) = {g_final:.8f}")
        
        # Check if solution is accurate
        if abs(f_final) < 1e-6 and abs(g_final) < 1e-6:
            print("✓ Solution is accurate!")
        else:
            print("⚠ Solution may not be accurate enough.")
            
    except Exception as e:
        print(f"Error in verification: {e}")
else:
    print("Solution failed due to singular Jacobian or other errors.")