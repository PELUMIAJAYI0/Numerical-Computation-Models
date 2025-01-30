import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.01  # Thermal diffusivity
dx = 0.01     # Space step
dt = 0.0001   # Time step (stability condition: dt < dx^2 / 2*alpha)
L = 1.0       # Length of the panel
T_max = 0.1   # Simulation time
nx = int(L/dx)  # Number of spatial points
nt = int(T_max/dt)  # Number of time steps

# Initial temperature distribution
T = np.zeros(nx)
T[int(nx/2)] = 100  # Heat source in the middle

# Precompute constant factor
factor = alpha * dt / dx**2

# Time stepping loop
for n in range(nt):
    T_new = T.copy()
    T_new[1:-1] = T[1:-1] + factor * (T[:-2] - 2*T[1:-1] + T[2:])  # Vectorized update
    T = T_new.copy()

# Plot final temperature distribution
plt.plot(np.linspace(0, L, nx), T, color='red', linewidth=2, label='Final Temperature')
plt.xlabel("Position along solar panel (m)")
plt.ylabel("Temperature (°C)")
plt.title("Heat Distribution in Solar Panel")
plt.legend()
plt.grid()
plt.show()
