def gauss_seidel(a, b, x0, tol=1e-4, max_iterations=100):
    n = len(a)
    x = x0.copy()

    print("\nGauss-Seidel Iteration:\n")
    for iteration in range(1, max_iterations + 1):
        x_old = x.copy()

        for i in range(n):
            sum_ = b[i]
            for j in range(n):
                if j != i:
                    sum_ -= a[i][j] * x[j]
            x[i] = sum_ / a[i][i]

        print(f"Iteration {iteration}: ", end="")
        for i in range(n):
            print(f"x{i+1} = {x[i]:.6f}  ", end="")
        print()

        # Check for convergence
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            break

    print("\nSolution after", iteration, "iterations:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")


# === USER INPUT ===
n = int(input("Enter the number of equations: "))

a = []
b = []
x0 = []

print("\nEnter the coefficients of each equation (including RHS):")
for i in range(n):
    row = list(map(float, input(f"Equation {i+1} (a1 a2 ... an b): ").split()))
    if len(row) != n + 1:
        print("Invalid input. Try again.")
        exit()
    a.append(row[:-1])
    b.append(row[-1])

print("\nEnter initial guesses for the variables (x1 x2 ... xn):")
x0 = list(map(float, input().split()))
if len(x0) != n:
    print("Invalid input for initial guesses.")
    exit()

gauss_seidel(a, b, x0)