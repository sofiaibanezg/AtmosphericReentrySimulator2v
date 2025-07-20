# src/Simulator.py

from Capsule import Capsule
import matplotlib.pyplot as plt


class ReentrySimulator:
    def __init__(self, capsule, atmosphere, dt=1.0):
        self.capsule = capsule
        self.atmosphere = atmosphere
        self.dt = dt  # passage of time in seconds
        self.time = 0  # total time simulation
        self.data_log = []

    def compute_drag_force(self, velocity, altitude):
        rho = self.atmosphere.get_density(altitude)
        A = self.capsule.area
        Cd = self.capsule.drag_coefficient
        return 0.5 * rho * A * Cd * velocity**2

    def step(self):
        g = 9.81  # Constant gravity, approximate general value
        m = self.capsule.mass
        v = self.capsule.velocity
        h = self.capsule.altitude

        drag = self.compute_drag_force(abs(v), h)
        direction = -1 if v < 0 else 1  # drag direction

        # Newton's second law: F = m * a => a = F_net / m
        # F_net = Capsule weight + drag force (drag's direction depends on the direction of movement)
        # So: a = -g + (direction * drag) / m
        # If the capsule falls (v < 0), drag opposes, and direction = -1
        # If the capsule rose (v > 0), drag opposes, and direction = +1
        a = -g + direction * (drag / m)

        v += a * self.dt
        h += v * self.dt

        # Simplified temperature as a function of velocity
        temp = self.capsule.temperature + 0.02 * abs(v)

        # Update the status
        self.capsule.velocity = v
        self.capsule.altitude = max(h, 0)
        self.capsule.temperature = temp

        self.time += self.dt
        self.data_log.append((self.time, h, v, temp))

    def run(self):
        print("Simulation started\n")
        while not self.capsule.is_landed():
            self.step()
            print(self.capsule)  # Muestra estado actual
        print("\nCapsule has landed, congrats.")

    def plot_results(self):
        times = [entry[0] for entry in self.data_log]
        altitudes = [entry[1] for entry in self.data_log]
        velocities = [entry[2] for entry in self.data_log]
        temperatures = [entry[3] for entry in self.data_log]

        plt.figure(figsize=(12, 8))

        plt.subplot(3, 1, 1)
        plt.plot(times, altitudes, label="Altitude (m)", color='blue')
        plt.ylabel("Altitude (m)")
        plt.grid(True)

        plt.subplot(3, 1, 2)
        plt.plot(times, velocities, label="Velocity (m/s)", color='red')
        plt.ylabel("Velocity (m/s)")
        plt.grid(True)

        plt.subplot(3, 1, 3)
        plt.plot(times, temperatures, label="Temperature (K)", color='orange')
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (K)")
        plt.grid(True)

        plt.tight_layout()
        plt.suptitle("Reentry Simulation Results", fontsize=16, y=1.02)
        plt.show()
