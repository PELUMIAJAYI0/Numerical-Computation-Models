

# Constants
rho = 1.225  # Air density in kg/m^3
A = 100      # Swept area of the wind turbine in m^2
v = 12       # Wind speed in m/s

# Kinetic Energy Calculation (Power from Wind)
P_wind = 0.5 * rho * A * v**3

# Turbine Efficiency (assuming energy output is 40% of the wind energy)
efficiency = 0.4  # Example efficiency
P_turbine = P_wind * efficiency

# Results
print(f"Power from wind: {P_wind} W")
print(f"Power output from turbine: {P_turbine} W")
