import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Constants
battery_capacity = 10000  # Battery capacity in Wh (10 kWh)
charging_efficiency = 0.9  # 90% efficiency during charging
discharging_efficiency = 0.85  # 85% efficiency during discharging
round_trip_efficiency = charging_efficiency * discharging_efficiency  # Overall efficiency of storage system

# Parameters for the model
charging_power = 3000  # Charging power in W (3 kW)
discharging_power = 2500  # Discharging power in W (2.5 kW)
initial_soc = 0.2  # Initial state of charge (20% of full capacity)
time_period = 24  # Simulate over 24 hours (1 day)

# Energy usage pattern (idealized based on solar/wind generation)
# For simplicity, assuming this is generated from renewable systems like solar/wind.
energy_demand = np.zeros(time_period)
energy_demand[6:18] = 1500  # High demand during daytime (6 AM to 6 PM)
energy_demand[18:6] = 500  # Lower demand at night (6 PM to 6 AM)

# Function to simulate battery performance (charging/discharging)
def battery_performance(x):
    """
    Simulate the performance of a battery system over a given period.
    Optimize the charging/discharging cycle for maximum efficiency.
    
    Parameters:
    - x: Array containing charging times (hours) and discharging times (hours).
    
    Returns:
    - Negative total efficiency (to minimize the negative of efficiency, maximizing the efficiency).
    """
    charging_times = x[0]  # Charging hours
    discharging_times = x[1]  # Discharging hours
    
    # Calculate energy charge and discharge based on time and efficiency
    energy_charged = charging_times * charging_power * charging_efficiency  # Energy charged into battery (Wh)
    energy_discharged = discharging_times * discharging_power * discharging_efficiency  # Energy discharged (Wh)
    
    # Adjust for the battery capacity and round-trip efficiency
    energy_stored = min(energy_charged, battery_capacity - initial_soc * battery_capacity)  # Capacity constraint
    energy_used = min(energy_discharged, energy_stored)
    
    # Calculate the total energy delivered by the battery
    total_energy_delivered = energy_used * round_trip_efficiency
    
    # Total efficiency: Energy delivered divided by total energy charged
    total_efficiency = total_energy_delivered / energy_charged if energy_charged > 0 else 0
    
    # The objective is to maximize efficiency, so we minimize the negative of efficiency
    return -total_efficiency

# Initial guess for optimization: 8 hours of charging, 8 hours of discharging
initial_guess = [8, 8]

# Optimization using SciPy
result = opt.minimize(battery_performance, initial_guess, bounds=[(0, time_period), (0, time_period)])

# Extract the optimized values
optimized_charging_times = result.x[0]
optimized_discharging_times = result.x[1]

# Calculate the total efficiency with optimized times
optimized_efficiency = -result.fun

# Display the results
print(f"Optimized Charging Time: {optimized_charging_times:.2f} hours")
print(f"Optimized Discharging Time: {optimized_discharging_times:.2f} hours")
print(f"Optimized System Efficiency: {optimized_efficiency*100:.2f}%")

# Visualization of Energy Charge and Discharge Over Time
time = np.arange(time_period)
battery_soc = np.zeros(time_period)
battery_soc[0] = initial_soc * battery_capacity

for t in range(1, time_period):
    if t < optimized_charging_times:  # Charging phase
        battery_soc[t] = battery_soc[t-1] + charging_power * charging_efficiency
    elif t < optimized_charging_times + optimized_discharging_times:  # Discharging phase
        battery_soc[t] = battery_soc[t-1] - discharging_power * discharging_efficiency
    else:
        battery_soc[t] = battery_soc[t-1]  # No charge/discharge outside optimized times
    
    # Ensure battery capacity is within bounds
    battery_soc[t] = np.clip(battery_soc[t], 0, battery_capacity)

# Plotting the battery state of charge (SOC) over time
plt.figure(figsize=(10, 6))
plt.plot(time, battery_soc, label='Battery State of Charge (SOC)', color='blue')
plt.axvline(x=optimized_charging_times, color='green', linestyle='--', label='Optimized Charging Period')
plt.axvline(x=optimized_charging_times + optimized_discharging_times, color='red', linestyle='--', label='Optimized Discharging Period')
plt.xlabel('Time (Hours)')
plt.ylabel('State of Charge (Wh)')
plt.title('Optimized Battery Performance')
plt.legend()
plt.grid(True)
plt.show()
