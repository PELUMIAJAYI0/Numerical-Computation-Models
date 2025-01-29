import matplotlib.pyplot as plt
import numpy as np

rho = 1.225  # Air density in kg/m^3
A = 100      # Swept area of the wind turbine in m^2
v = 12       # Wind speed in m/

wind_speeds = np.linspace(5, 25, 20)  # Range of wind speeds
efficiencies = 0.4 * (0.5 * rho * A * wind_speeds**3)  # Example efficiency at each wind speed

plt.plot(wind_speeds, efficiencies)
plt.title("Wind Turbine Efficiency vs Wind Speed")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Efficiency (W)")
plt.grid(True)
plt.show()
