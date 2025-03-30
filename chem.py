import numpy as np
import matplotlib.pyplot as plt

# Constants
k1 = 0.1  # Rate constant for forward reaction (A -> B)
k2 = 0.05  # Rate constant for backward reaction (B -> A)

time_steps = 1000  # Number of time steps
dt = 0.1  # Time increment

# Initial concentrations
A = 1.0  # Initial concentration of A
B = 0.0  # Initial concentration of B

# Arrays to store concentrations over time
time = np.arange(0, time_steps * dt, dt)
A_conc = np.zeros(time_steps)
B_conc = np.zeros(time_steps)

# Simulation loop
for t in range(time_steps):
    dA = -k1 * A * dt + k2 * B * dt
    dB = k1 * A * dt - k2 * B * dt

    A += dA
    B += dB

    A_conc[t] = A
    B_conc[t] = B

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(time, A_conc, label='[A]', color='blue')
plt.plot(time, B_conc, label='[B]', color='red')
plt.title('Chemical Reaction Simulation: A ⇌ B')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.grid()
plt.show()
