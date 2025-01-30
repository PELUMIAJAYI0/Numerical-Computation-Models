import numpy as np
import matplotlib.pyplot as plt

# Grid size
nx, ny = 100, 50
u = np.zeros((nx, ny))  # Velocity field

# Define an obstacle (simulating turbine blade)
blade_x, blade_y = 50, 25
radius = 5

# Apply simple boundary conditions
for i in range(nx):
    for j in range(ny):
        if (i-blade_x)**2 + (j-blade_y)**2 < radius**2:
            u[i, j] = 0  # No wind inside the blade

# Simulate simple wind flow
for t in range(10):  # Time steps
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            if u[i, j] != 0:  # Avoid updating obstacle
                u[i, j] = 0.5 * (u[i-1, j] + u[i+1, j])  # Simplified update

# Visualizing the wind flow
plt.imshow(u.T, cmap="coolwarm", origin="lower")
plt.colorbar(label="Wind Speed")
plt.title("Wind Flow Around a Turbine Blade")
plt.show()
