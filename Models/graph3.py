import matplotlib.pyplot as plt

opt_values = 25
solar_capacity = 678
wind_capacity = 890
storage_capacity = 67

categories = ['Solar', 'Wind', 'Storage']
values = [opt_values*solar_capacity, opt_values*wind_capacity, opt_values*storage_capacity]

plt.bar(categories, values)
plt.title("Optimal Hybrid Energy System Contribution")
plt.xlabel("Energy Source")
plt.ylabel("Capacity (kW or kWh)")
plt.grid(False)
plt.show()
