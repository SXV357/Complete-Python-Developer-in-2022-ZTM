import matplotlib.pyplot as plt
import numpy as np

class Particle():
    def __init__(self, position, velocity, acceleration, mass):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass

    def update_position(self, dt):
        self.position += self.velocity * dt + 0.5 * self.acceleration * dt ** 2

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt

    def update_acceleration(self, force):
        self.acceleration = force / self.mass

    def update(self, dt, force):
        self.update_acceleration(force)
        self.update_velocity(dt)
        self.update_position(dt)

    def get_position(self):
        return self.position
    
    def get_velocity(self):
        return self.velocity
    
    def get_acceleration(self):
        return self.acceleration

    def print_final_pos_vel_acc(self):
        print('Final position: ', self.get_position(), "m")
        print('Final velocity: ', self.get_velocity(), "m/s")
        print('Final acceleration: ', self.get_acceleration(), "m/s^2")

    def plot_position(self, dt):
        time = np.arange(0, 10, dt)
        position = []
        for t in time:
            position.append(self.get_position())
            self.update(dt, 1)
        plt.plot(time, position)
        plt.xlabel('Time (s)')
        plt.ylabel('Position (m)')
        plt.show()

    def plot_velocity(self, dt):
        time = np.arange(0, 10, dt)
        velocity = []
        for t in time:
            velocity.append(self.get_velocity())
            self.update(dt, 1)
        plt.plot(time, velocity)
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.show()

p1 = Particle(0, 0, 0, 1)
p1.plot_position(0.01)
p1.plot_velocity(0.01)
p1.print_final_pos_vel_acc()
