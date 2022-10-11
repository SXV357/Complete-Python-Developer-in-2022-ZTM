import numpy as np
import matplotlib.pyplot as plt

vox = 40
voy = 30
x0 = 0
ax = 0
g = 9.81
yf = -35

# plot position vs time
t = np.arange(0, 10, 0.01)
x = vox * t + 0.5 * ax * t ** 2
y = voy * t + 0.5 * -g * t ** 2
plt.plot(t, x, label='Horizontal positon', color='red')
plt.plot(t, y, label='Vertical position', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()

# plot velocity vs time
t = np.arange(0, 10, 0.01)
vx = vox + ax * t
vy = voy + -g * t
plt.plot(t, vx, label='Horizontal velocity', color='red')
plt.plot(t, vy, label='Vertical velocity', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()
