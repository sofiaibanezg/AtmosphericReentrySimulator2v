# src/Capsule.py

class Capsule:
    def __init__(self, mass, area, drag_coefficient):
        self.mass = mass  # kg
        self.area = area  # m^2
        self.drag_coefficient = drag_coefficient
        self.altitude = 120000  # m
        self.velocity = -100    # m/s (negative = descending)
        self.temperature = 300  # K

    def is_landed(self):
        return (self.altitude <= 0)

    def __str__(self):
        return f"Altitud: {self.altitude} m | Velocidad: {self.velocity} m/s | Temp: {self.temperature} K"
