import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation Parameters
# -----------------------------
dt = 0.1              # time step (seconds)
total_time = 20       # total simulation time (seconds)
time_steps = int(total_time / dt)

# -----------------------------
# True Aircraft Motion
# -----------------------------
x_true = np.zeros(time_steps)
y_true = np.zeros(time_steps)

vx = 5    # velocity in x (m/s)
vy = 3    # velocity in y (m/s)

for i in range(1, time_steps):
    x_true[i] = x_true[i-1] + vx * dt
    y_true[i] = y_true[i-1] + vy * dt

print("Motion simulation complete.")
