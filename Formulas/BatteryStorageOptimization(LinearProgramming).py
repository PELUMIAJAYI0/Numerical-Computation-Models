from scipy.optimize import linprog

# Cost coefficients: Lower is better
C = [0.1, 0.2, 0.05]  # Cost per unit energy

# Constraints: S + W - B = Demand (10 units)
A_eq = [[1, 1, -1]]  
b_eq = [10]

# Bounds: Non-negative energy production
bounds = [(0, None), (0, None), (0, None)]

# Solve optimization problem
result = linprog(C, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Display results
print("\n=== Optimized Renewable Energy Distribution ===")
print(f" Solar Energy Used: {result.x[0]:.2f} units")
print(f" Wind Energy Used: {result.x[1]:.2f} units")
print(f" Battery Storage Used: {result.x[2]:.2f} units")
print(f" Total Cost: {result.fun:.2f} currency units")
