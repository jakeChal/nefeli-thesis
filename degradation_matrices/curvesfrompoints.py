import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# # Original data
# data = {
#     "WL-EPS 1-S": [2.498, 2.004, 1.497, 1.454, 1.452],
#     "WL-EPS 1-1": [2.222, 1.725, 1.370, 1.346, 1.322],
#     "WL-EPS 2-S": [2.158, 1.825, 1.486, 1.535, 1.535],
#     "WL-EPS 2-2": [1.968, 1.671, 1.578, 1.453, 1.450],
#     "WN-EPS 1-S": [2.485, 1.965, 1.493, 1.469, 1.424],
#     "WN-EPS 1-1": [2.221, 1.687, 1.368, 1.367, 1.338],
#     "WN-EPS 2-S": [2.157, 1.860, 1.694, 1.588, 1.575],
#     "WN-EPS 2-2": [1.984, 1.698, 1.566, 1.471, 1.472],
#     "WL-XPS 40K": [2.661, 2.522, 2.094, 1.913, 1.902],
#     "WL-XPS 50K": [2.579, 2.445, 2.044, 1.903, 1.897],
#     "WN-XPS 40K": [2.656, 2.486, 2.128, 1.992, 1.929],
#     "WN-XPS 50K": [2.613, 2.476, 2.128, 2.048, 2.024]
# }

# # Normalize data
# normalized_data = {}
# for material, values in data.items():
#     first_value = values[0]
#     normalized_values = [val / first_value for val in values]
#     normalized_data[material] = normalized_values

# # Separate data for XPS and EPS materials
# xps_data = {key: value for key, value in normalized_data.items() if 'XPS' in key}
# eps_data = {key: value for key, value in normalized_data.items() if 'EPS' in key}

# # Calculate mean curves for XPS and EPS
# mean_xps_values = np.mean(list(xps_data.values()), axis=0)
# mean_eps_values = np.mean(list(eps_data.values()), axis=0)

# # Plotting original data
# plt.figure(figsize=(15, 5))
# plt.subplot(1, 3, 1)
# plt.title('Original Data')
# for material, values in data.items():
#     x_data = [0, 100, 1000, 4000, 5000]  # Days
#     y_data = values  # Original data
#     plt.plot(x_data, y_data, label=material)
# plt.xlabel('Days')
# plt.ylabel('Deterioration ratio (%)')
# plt.legend()

# # Plotting normalized data
# plt.subplot(1, 3, 2)
# plt.title('Normalized Data')
# for material, values in normalized_data.items():
#     x_data = [0, 100, 1000, 4000, 5000]  # Days
#     y_data = values  # Normalized data
#     plt.plot(x_data, y_data, label=material)
# plt.xlabel('Days')
# plt.ylabel('Normalized Deterioration ratio')
# plt.legend()

# # Plotting mean curves
# plt.subplot(1, 3, 3)
# plt.title('Mean Curves')
# x_data = [0, 100, 1000, 4000, 5000]  # Days
# plt.plot(x_data, mean_xps_values, marker='o', linestyle='-', color='black', label='Mean Curve (XPS)')
# plt.plot(x_data, mean_eps_values, marker='o', linestyle='-', color='red', label='Mean Curve (EPS)')
# plt.xlabel('Days')
# plt.ylabel('Normalized Deterioration ratio')
# plt.legend()

# plt.tight_layout()
# plt.show()

# # Plot linear regression lines for EPS
# plt.figure(figsize=(8, 6))
# plt.title('Linear Regression Lines (EPS)')
# x_data_eps = [0, 100, 1000, 4000, 5000]
# slope_1, intercept_1 = np.polyfit(x_data_eps[:3], mean_eps_values[:3], 1)
# slope_2, intercept_2 = np.polyfit(x_data_eps[2:], mean_eps_values[2:], 1)
# plt.plot(x_data_eps[:3], slope_1 * np.array(x_data_eps[:3]) + intercept_1, 'r-', label='Linear Regression (EPS: 0 to 1000 days)')
# plt.plot(x_data_eps[2:], slope_2 * np.array(x_data_eps[2:]) + intercept_2, 'b-', label='Linear Regression (EPS: 1000 to 5000 days)')
# plt.xlabel('Days')
# plt.ylabel('Normalized Deterioration ratio')
# plt.legend()
# plt.grid(True)
# plt.show()







import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



time_points = [0,5,100,1000,4000,5000]

# Original data
data = {
    "WL-EPS 1-S": [2.498, 2.498, 2.004, 1.497, 1.454, 1.452],
    "WL-EPS 1-1": [2.222, 2.222, 1.725, 1.370, 1.346, 1.322],
    "WL-EPS 2-S": [2.158, 2.158, 1.825, 1.486, 1.535, 1.535],
    "WL-EPS 2-2": [1.968, 1.968, 1.671, 1.578, 1.453, 1.450],
    "WN-EPS 1-S": [2.485, 2.485, 1.965, 1.493, 1.469, 1.424],
    "WN-EPS 1-1": [2.221, 2.221, 1.687, 1.368, 1.367, 1.338],
    "WN-EPS 2-S": [2.157, 2.157, 1.860, 1.694, 1.588, 1.575],
    "WN-EPS 2-2": [1.984, 1.984, 1.698, 1.566, 1.471, 1.472]
}

# Initialize lists to store normalized values and distinct days
normalized_values = []

# Iterate through each row
for row in data.values():
    # Calculate initial value for normalization
    initial_value = row[0]

    # Normalize each day value and append to the normalized values list
    normalized_row = [(initial_value - value) / initial_value for value in row]
    normalized_values.append(normalized_row)

# Convert the normalized values list to a NumPy array
normalized_array = np.array(normalized_values)

# Calculate the mean along the columns (axis 0)
mean_values = np.mean(normalized_array, axis=0)

print("Mean values of each column:", mean_values)


# Calculate the standard deviation along the columns (axis 0)
std_dev_values = np.std(normalized_array, axis=0)

print("Standard deviation of each column:", std_dev_values)


# Convert the mean values to represent percentages
percentage_mean_values = (1 - mean_values) * 100




# Logarithmic function
def logarithmic_function(t, a, b):
    return a * np.log(b * t + 1)

# Fit the logarithmic curve to the data
popt_logarithmic, _ = curve_fit(logarithmic_function, time_points, mean_values)

# Generate time points for the curve (days)
time_curve_days = np.linspace(min(time_points), max(time_points), 1000)

# Calculate degradation values for the main logarithmic curve (days)
degradation_logarithmic_days = logarithmic_function(time_curve_days, *popt_logarithmic)

# # Calculate variance of day 5000 values
# day_5000_values = [row[-1] for row in normalized_values]
# variance_day_5000 = np.var(day_5000_values)

# # Calculate upper and lower bounds by adding and subtracting variance from the main curve
# upper_bound_days = degradation_logarithmic_days + np.sqrt(variance_day_5000)
# lower_bound_days = degradation_logarithmic_days - np.sqrt(variance_day_5000)

# Calculate degradation values for each year using the fitted logarithmic curve
degradation_logarithmic_years = logarithmic_function(time_curve_days, *popt_logarithmic)

popt_above = np.copy(popt_logarithmic)
popt_above[0] = popt_above[0] * 0.7
degradation_logarithmic_days_above = logarithmic_function(time_curve_days, *popt_above)

popt_below = np.copy(popt_logarithmic)
popt_below[0] = popt_below[0] * 1.1
degradation_logarithmic_days_below = logarithmic_function(time_curve_days, *popt_below)


# Plot the main logarithmic curve (days)
plt.figure(figsize=(10, 6))
plt.plot(time_curve_days, degradation_logarithmic_days, 'm-', label='Main Logarithmic Curve (Days)')
plt.fill_between(time_curve_days, degradation_logarithmic_days_below, degradation_logarithmic_days_above, color='gray', alpha=0.2, label='Range (±1 Standard Deviation)')
plt.xlabel('Time (days)')
plt.ylabel('Degradation')
plt.title('Main Logarithmic Curve with Range (Days)')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()



# Logarithmic function
def logarithmic_function(t, a, b):
    return a * np.log(b * t + 1)

# Generate time points for the new curve (years)
time_curve_years = np.linspace(0, 150, 1000)

# Fit the logarithmic curve to the data
popt_logarithmic, _ = curve_fit(logarithmic_function, time_points, mean_values)


# Calculate degradation values for each year using the fitted logarithmic curve
degradation_logarithmic_years = logarithmic_function(time_curve_years * 365, *popt_logarithmic)

popt_above = np.copy(popt_logarithmic)
popt_above[0] = popt_above[0] * 0.7
degradation_logarithmic_years_above = logarithmic_function(time_curve_years * 365, *popt_above)

popt_below = np.copy(popt_logarithmic)
popt_below[0] = popt_below[0] * 1.1
degradation_logarithmic_years_below = logarithmic_function(time_curve_years * 365, *popt_below)

# Calculate variance at each time point
variance_years = np.linspace(0, 0.01, 1000)  # Example: variance increases linearly over time

# Calculate upper and lower bounds by adding and subtracting variance from the main curve
upper_bound_years = degradation_logarithmic_years + np.sqrt(variance_years)
lower_bound_years = degradation_logarithmic_years - np.sqrt(variance_years)

# Plot the main logarithmic curve (years) with widening upper and lower bounds
plt.figure(figsize=(10, 6))
plt.plot(time_curve_years, degradation_logarithmic_years, 'g-', label='Main Logarithmic Curve (Years)')
# plt.plot(time_curve_years, degradation_logarithmic_years_above, 'b-', label='Above Logarithmic Curve (Years)')
# plt.plot(time_curve_years, degradation_logarithmic_years_below, 'y-', label='Brlow Logarithmic Curve (Years)')

plt.fill_between(time_curve_years, degradation_logarithmic_years_below, degradation_logarithmic_years_above, color='gray', alpha=0.2, label='Range (±1 Standard Deviation)')
plt.xlabel('Time (years)')
plt.ylabel('Degradation')
plt.title('Main Logarithmic Curve with Widening Range (Years)')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()
