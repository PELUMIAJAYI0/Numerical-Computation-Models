import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Constants
time_period = 24  # Simulating over 24 hours (1 day)
grid_price = 0.15  # Grid electricity price in $/kWh (example)
battery_capacity = 10  # Battery capacity in kWh
solar_power_max = 6  # Maximum solar power output in kW (ideal conditions)
wind_power_max = 5  # Maximum wind power output in kW (ideal conditions)
charging_efficiency = 0.9  # Battery charging efficiency
discharging_efficiency = 0.85  # Battery discharging efficiency
initial_battery_soc = 0.2  # Initial battery state of charge (20%)

# Energy Consumption Profile (kW)
energy_demand = np.zeros(time_period)
energy_demand[6:18] = 5  # 5 kW demand during the daytime (6 AM to 6 PM)
energy_demand[18:6] = 3  # 3 kW demand at night (6 PM to 6 AM)

# Renewable Energy Profile (solar and wind power in kW)
solar_power = np.zeros(time_period)
wind_power = np.zeros(time_period)

# Solar power is available during the day (6 AM to 6 PM)
solar_power[6:18] = np.random.uniform(0, solar_power_max, 12)

# Wind power is available throughout the day with some fluctuations
wind_power = np.random.uniform(0, wind_power_max, time_period)

# Function to simulate energy management (minimizing costs)
def energy_management(x):
    """
    Optimize the energy consumption and battery storage usage to minimize costs and maximize renewable energy usage.
    
    Parameters:
    - x: Array containing grid power usage and battery charge/discharge values.
    
    Returns:
    - Negative total cost (minimize the negative of the cost, maximizing the savings).
    """
    # Extract grid power usage, battery charge/discharge
    grid_usage = x[:time_period]  # Grid usage in kW
    battery_charge = x[time_period:2*time_period]  # Battery charging in kW
    battery_discharge = x[2*time_period:]  # Battery discharging in kW
    
    total_cost = 0
    total_savings = 0
    
    battery_soc = np.zeros(time_period)
    battery_soc[0] = initial_battery_soc * battery_capacity
    
    # Calculate total cost and savings based on energy usage and renewable energy utilization
    for t in range(1, time_period):
        # Energy consumption balance: Total demand should be satisfied by solar, wind, battery, and grid
        renewable_energy = solar_power[t] + wind_power[t]  # Total renewable energy available at time t
        total_demand = energy_demand[t]
        
        # Calculate battery charging/discharging
        energy_from_battery = battery_discharge[t] * discharging_efficiency if battery_soc[t-1] > 0 else 0
        energy_used_from_grid = grid_usage[t]  # Energy needed from the grid
        
        # Adjust battery SOC (state of charge)
        battery_soc[t] = battery_soc[t-1] + battery_charge[t] * charging_efficiency - battery_discharge[t]
        battery_soc[t] = np.clip(battery_soc[t], 0, battery_capacity)  # Battery capacity limit
        
        # Balance the energy consumption: Use renewable, then battery, then grid
        energy_used_from_renewables = min(renewable_energy, total_demand)
        remaining_demand = total_demand - energy_used_from_renewables
        
        energy_used_from_battery = min(remaining_demand, energy_from_battery)
        remaining_demand -= energy_used_from_battery
        
        energy_used_from_grid = min(remaining_demand, energy_used_from_grid)
        
        # Cost calculation: Grid electricity has a cost
        total_cost += energy_used_from_grid * grid_price
        total_savings += energy_used_from_renewables  # Savings from using renewable energy instead of grid
        
    # The objective is to minimize the total cost while maximizing renewable energy usage
    return total_cost - total_savings

# Initial guess for optimization: assuming we use the grid to fulfill all the demand initially
initial_guess = np.zeros(3 * time_period)
initial_guess[:time_period] = energy_demand  # Assume we use grid for all the energy demand initially

# Bounds for optimization: grid usage, battery charging/discharging within practical limits
bounds = [(0, max(solar_power_max, wind_power_max))] * time_period + [(0, battery_capacity)] * time_period + [(0, battery_capacity)] * time_period

# Perform optimization using SciPy
result = opt.minimize(energy_management, initial_guess, bounds=bounds)

# Extract the optimized values
optimized_grid_usage = result.x[:time_period]
optimized_battery_charge = result.x[time_period:2*time_period]
optimized_battery_discharge = result.x[2*time_period:]

# Total optimized cost
optimized_cost = result.fun

# Display the results
print(f"Optimized Total Cost: ${optimized_cost:.2f}")

# Visualization of Energy Usage: Grid, Battery, Renewable energy
time = np.arange(time_period)

plt.figure(figsize=(12, 6))
plt.plot(time, energy_demand, label='Energy Demand (kW)', color='black', linestyle='--')
plt.plot(time, optimized_grid_usage, label='Grid Power Usage (kW)', color='red')
plt.plot(time, optimized_battery_discharge, label='Battery Discharge (kW)', color='blue')
plt.plot(time, solar_power + wind_power, label='Renewable Energy (kW)', color='green')
plt.xlabel('Time (Hours)')
plt.ylabel('Power (kW)')
plt.title('Optimized Energy Management and Load Profile')
plt.legend()
plt.grid(True)
plt.show()
