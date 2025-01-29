# Constants
G = 1000  # Solar irradiance in W/m^2
A_panel = 1.6  # Area of the panel in m^2
eta = 0.18  # Efficiency of the solar panel

# Calculate the power output
P_solar = eta * G * A_panel
print(f"Solar Panel Power Output: {P_solar} W")
