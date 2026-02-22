import numpy as np          # For arrays and maths
import matplotlib.pyplot as plt  # For plotting graphs
import pandas as pd  # For saving data as CSV
# -----------------------------
# Simulation Parameters
# -----------------------------
time_steps = 100            # Number of time steps in the simulation
vx = 1.0                    # Velocity in x-direction (m/s)
vy = 0.5                    # Velocity in y-direction (m/s)
noise_std = 2.0             # Standard deviation of radar measurement noise

# -----------------------------
# True Motion Model
# -----------------------------
# This calculates the aircraft's real position at each time step
true_x = []
true_y = []

for t in range(time_steps):
    x = vx * t
    y = vy * t
    true_x.append(x)
    true_y.append(y)

# -----------------------------
# Radar Measurements (Noisy)
# -----------------------------
# Adds simulated noise to represent real radar inaccuracies
measured_x = []
measured_y = []

for i in range(time_steps):
    noisy_x = true_x[i] + np.random.normal(0, noise_std)
    noisy_y = true_y[i] + np.random.normal(0, noise_std)
    measured_x.append(noisy_x)
    measured_y.append(noisy_y)

# -----------------------------
# Moving Average Filter
# -----------------------------
# Smooths out the noisy radar data to estimate the true path
window_size = 5             # How many measurements to average over
filtered_x = []
filtered_y = []

for i in range(time_steps):
    start_index = max(0, i - window_size + 1)
    avg_x = np.mean(measured_x[start_index:i+1])
    avg_y = np.mean(measured_y[start_index:i+1])
    filtered_x.append(avg_x)
    filtered_y.append(avg_y)

# -----------------------------
# Error Analysis (MSE)
# -----------------------------
# Compare measured and filtered positions to the true positions
true_x_arr = np.array(true_x)
true_y_arr = np.array(true_y)
measured_x_arr = np.array(measured_x)
measured_y_arr = np.array(measured_y)
filtered_x_arr = np.array(filtered_x)
filtered_y_arr = np.array(filtered_y)

mse_measured = np.mean((true_x_arr - measured_x_arr)**2 +
                       (true_y_arr - measured_y_arr)**2)
mse_filtered = np.mean((true_x_arr - filtered_x_arr)**2 +
                       (true_y_arr - filtered_y_arr)**2)

improvement = ((mse_measured - mse_filtered) / mse_measured) * 100

print("MSE (Measured):", mse_measured)
print("MSE (Filtered):", mse_filtered)
print("Improvement (%):", improvement)
# Create a table with all position data
df = pd.DataFrame({
    "TimeStep": range(time_steps),
    "True_X": true_x,
    "True_Y": true_y,
    "Measured_X": measured_x,
    "Measured_Y": measured_y,
    "Filtered_X": filtered_x,
    "Filtered_Y": filtered_y
})

# Save the table as a CSV file
df.to_csv("radar_tracking_data.csv", index=False)
print("CSV file saved.")
# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(10,6))  # Make plot bigger and clearer

# Plot true path
plt.plot(true_x, true_y, color='blue', linewidth=2)

# Plot noisy measurements
plt.scatter(measured_x, measured_y, color='red', s=20, alpha=0.6)

# Plot filtered path
plt.plot(filtered_x, filtered_y, color='green', linewidth=2, linestyle='--')

# Titles and labels
plt.title("Radar Tracking Simulation", fontsize=16)
plt.xlabel("X Position (m)", fontsize=12)
plt.ylabel("Y Position (m)", fontsize=12)

plt.legend(["True Path", "Measured Path", "Filtered Path"])
plt.grid(True)

# Save high-quality image
plt.savefig("radar_tracking_plot.png", dpi=300)

# Show plot
plt.show()