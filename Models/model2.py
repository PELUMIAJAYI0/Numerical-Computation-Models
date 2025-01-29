import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Constants
solar_irradiance = 1000  # W/m^2 (average solar irradiance under clear sky conditions)
panel_area = 20  # m^2 (area of the solar panel)
panel_efficiency = 0.18  # 18% efficiency of the solar panel
location_latitude = 35  # Latitude of the location (degrees)
time_of_day = 12  # 12 PM for maximum sunlight exposure
weather_variability = 0.2  # Variability in solar irradiance due to clouds

# Function to calculate solar power output
def solar_power_output(panel_area, solar_irradiance, panel_efficiency, angle):
    """
    Calculate the power output of a solar panel based on the angle, irradiance, and efficiency.
    
    Parameters:
    - panel_area: Area of the solar panel (m^2).
    - solar_irradiance: Solar irradiance in W/m^2.
    - panel_efficiency: Efficiency of the solar panel (0 to 1).
    - angle: Angle of the solar panel (degrees).
    
    Returns:
    - Power output in Watts (W).
    """
    # Correct irradiance based on panel angle (simplified model)
    angle_radians = np.radians(angle)
    adjusted_irradiance = solar_irradiance * np.cos(angle_radians)
    
    # Calculate the power output
    power_output = panel_area * adjusted_irradiance * panel_efficiency
    return power_output

# Objective Function for Optimization
def optimize_panel_angle(x):
    """
    Objective function to optimize the solar panel angle for maximum power output.
    
    Parameters:
    - x: Array containing the angle of the panel.
    
    Returns:
    - Negative power (to minimize the negative of power, maximizing the power).
    """
    angle = x[0]
    
    # Account for weather variability (Monte Carlo simulation)
    adjusted_irradiance = solar_irradiance * (1 + np.random.uniform(-weather_variability, weather_variability))
    
    # Calculate the power output
    return -solar_power_output(panel_area, adjusted_irradiance, panel_efficiency, angle)

# Initial guess for optimization: angle = 30 degrees
initial_guess = [30]

# Optimization using SciPy
result = opt.minimize(optimize_panel_angle, initial_guess, bounds=[(0, 90)])  # Bounds for panel angle: 0 to 90 degrees

# Extract the optimized value
optimized_angle = result.x[0]

# Calculate the power with optimized design
optimized_power = -result.fun  # The negative value is minimized in optimization

# Display the results
print(f"Optimized Panel Angle: {optimized_angle:.2f} degrees")
print(f"Optimized Power Output: {optimized_power:.2f} W")

# Visualization of Power Output vs. Angle
angles = np.linspace(0, 90, 100)
power_outputs = np.zeros(100)

# Run the Monte Carlo simulation for power output at different angles
for i, angle in enumerate(angles):
    power_outputs[i] = -optimize_panel_angle([angle])  # Negative of the minimized value

# Plotting the optimization result
plt.figure(figsize=(10, 6))
plt.plot(angles, power_outputs, label='Power Output', color='blue')
plt.scatter(optimized_angle, optimized_power, color='red', marker='x', label='Optimized Angle')
plt.xlabel('Panel Angle (Degrees)')
plt.ylabel('Power Output (W)')
plt.title('Solar Panel Optimization for Maximum Power Output')
plt.legend()
plt.grid(False)
plt.show()
