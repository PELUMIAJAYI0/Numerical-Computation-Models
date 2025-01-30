import numpy as np
import matplotlib.pyplot as plt

# Constants
eta = 0.9  # Efficiency
g = 9.81  # Gravity (m/s²)
H = 50  # Water head (m)
rho = 1000  # Water density (kg/m³)
Q = np.linspace(1, 20, 50)  # Flow rate from 1 to 20 m³/s

# Power calculation
P_hydro = eta * rho * g * Q * H

# Find max power flow rate
max_power_index = np.argmax(P_hydro)
optimal_flow = Q[max_power_index]

# Plot results
plt.plot(Q, P_hydro, color='green', linewidth=2, label="Hydropower Output")
plt.axvline(optimal_flow, color='red', linestyle="--", label=f"Optimal Flow Rate: {optimal_flow:.1f} m³/s")
plt.xlabel("Flow Rate (m³/s)")
plt.ylabel("Power Output (W)")
plt.title("Hydropower Generation vs Flow Rate")
plt.legend()
plt.grid()
plt.show()
