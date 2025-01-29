import numpy as np
import matplotlib.pyplot as plt

# constants 
G = 1000  # Solar irradiance in W/m^2
A_panel = 1.6  # Area of the panel in m^2
eta = 0.18  # Efficiency of the solar panel

# Calculate the power output
P_solar = eta * G * A_panel
print(f"Solar Panel Power Output: {P_solar} W")

irradiance = np.linspace(500, 1000, 10)  # Solar irradiance range
power_output = eta * irradiance * A_panel

plt.plot(irradiance, power_output)
plt.title("Solar Panel Power Output vs Solar Irradiance")
plt.xlabel("Solar Irradiance (W/m²)")
plt.ylabel("Power Output (W)")
plt.grid(True)
plt.show()
