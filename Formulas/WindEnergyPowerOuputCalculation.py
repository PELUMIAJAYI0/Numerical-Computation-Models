import numpy as np
import matplotlib.pyplot as plt

# Constants
rho = 1.225  # Air density (kg/m³)
R = 40  # Blade radius (m)
A = np.pi * R**2  # Swept area (m²)
Cp = 0.4  # Power coefficient (efficiency)
V = np.linspace(1, 20, 50)  # Wind speeds from 1 to 20 m/s

# Power calculation (vectorized)
P = 0.5 * rho * A * V**3 * Cp

# Find max power point
max_power_index = np.argmax(P)
optimal_speed = V[max_power_index]

# Plot power curve
plt.plot(V, P, marker='o', linestyle='-', color='blue', label="Power Output")
plt.axvline(optimal_speed, color='red', linestyle="--", label=f"Optimal Wind Speed: {optimal_speed:.1f} m/s")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Power Output (W)")
plt.title("Wind Turbine Power Output")
plt.legend()
plt.grid()
plt.show()
