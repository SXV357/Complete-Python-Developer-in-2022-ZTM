import numpy as np
import matplotlib.pyplot as plt

vox = 1
vfx = 1
voy = 0
x0 = 0
g = 9.81
ax = 0

# find initial height of projectile
y0 = round((vfx ** 2 - vox ** 2) / (2 * g), 3)
# yf = -50

#find time of flight
t = round((vfx - vox) / g, 3)

# # find final x position
# xf = round(vox * t + 0.5 * ax * t ** 2, 3)

# plot horizontal position vs time
t = np.arange(0, 10, 0.01)
x = x0 + (vox * t) + (0.5 * ax * t ** 2)
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Position-X (m)')
plt.show()

# plot vertical position vs time
t = np.arange(0, 10, 0.01)
y = y0 + (voy * t) + (0.5 * -g * t ** 2)
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Position-Y (m)')
plt.show()