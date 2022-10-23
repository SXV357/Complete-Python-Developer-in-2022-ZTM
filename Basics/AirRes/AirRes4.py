import math

b1 = 0.2
b2 = 0.8
vox = 40
voy = 30
vo = math.sqrt(vox ** 2 + voy ** 2)
theta = math.atan(voy / vox)
dt = 0.01
m1 = 0.5 # random number chosen for mass at the time
m2 = 1
ax = 0
g = 9.81

x1 = round((m1 / b1) * vo * math.cos(theta) * (1 - math.exp(-b1 * dt / m1)), 3)
x2 = round((m1 / b2) * vo * math.cos(theta) * (1 - math.exp(-b2 * dt / m1)), 3)

print("Distance travelled by particle with b = 0.2: ", x1, "m")

import matplotlib.pyplot as plt

t = 0
x = 0
x_list = []
t_list = []

while x < 1000:
     x = round((m1 / b1) * vo * math.cos(theta) * (1 - math.exp(-b1 * t / m1)), 3)
     x_list.append(x)
     t_list.append(t)
     t += dt

plt.plot(t_list, x_list)
plt.xlabel("Time (s)")
plt.ylabel("Horizontal distance (m)")
plt.show()

print("Distance travelled by particle with b = 0.8: ", x2, "m")

t = 0
x = 0
x_list = []
t_list = []

while x < 1000:
    x = round((m1 / b2) * vo * math.cos(theta) * (1 - math.exp(-b2 * t / m1)), 3)
    x_list.append(x)
    t_list.append(t)
    t += dt

plt.plot(t_list, x_list)
plt.xlabel("Time (s)")
plt.ylabel("Horizontal distance (m)")
plt.show()

# if x1 > x2:
#     print("Particle with b = 0.2 travels further.")
# elif x1 < x2:
#     print("Particle with b = 0.8 travels further.")
# else:
#     print("Particles travel the same distance.")

# print("Distance traveled for both drag coefficients with mass increased")

# x1 = round((m2 / b1) * vo * math.cos(theta) * (1 - math.exp(-b1 * dt / m2)), 3)
# x2 = round((m2 / b2) * vo * math.cos(theta) * (1 - math.exp(-b2 * dt / m2)), 3)

# print("Distance travelled by particle with b = 0.2: ", x1, "m")
# print("Distance travelled by particle with b = 0.8: ", x2, "m")

# if x1 > x2:
#     print("Particle with b = 0.2 travels further.")
# elif x1 < x2:
#     print("Particle with b = 0.8 travels further.")
# else:
#     print("Particles travel the same distance.")


# # using drag and force of gravity to calculate acceleration in y direction

# ay_general = round(-g - (b1 * voy) / m1, 3)
# ay_general2 = round(-g - (b2 * voy) / m1, 3)

# print("Acceleration in y direction for b = 0.2: ", ay_general, "m/s^2")
# print("Acceleration in y direction for b = 0.8: ", ay_general2, "m/s^2")

# # calculate time during which particle with acceleration ay_general will travel 1000 m

# t = round(1000 / (voy + 0.5 * ay_general * dt), 3)
# print("Time for particle with b = 0.2 to travel 1000 m: ", t, "s")
# t2 = round(1000 / (voy + 0.5 * ay_general2 * dt), 3)
# print("Time for particle with b = 0.8 to travel 1000 m: ", t2, "s")

# vfy1 = round(voy + ay_general * t, 3)
# vfy2 = round(voy + ay_general2 * t2, 3)

# print("Final velocity for particle with b = 0.2: ", vfy1, "m/s")
# print("Final velocity for particle with b = 0.8: ", vfy2, "m/s")

# create live animation of an object moving along a trajectory with air resistance

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()

ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = round((m1 / b1) * vo * math.cos(theta) * (1 - math.exp(-b1 * i / m1)), 3)
    y = round((m1 / b1) * vo * math.sin(theta) * (1 - math.exp(-b1 * i / m1)) - 0.5 * g * (i ** 2), 3)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=20, blit=True)

plt.show()