class Capsule:
    def __init__(self, mass, area, drag_coefficient):
        self.mass = mass  # kg
        self.area = area  # m^2
        self.drag_coefficient = drag_coefficient
        self.altitude = 120000  # m (inicia en 120 km)
        self.velocity = -100  # m/s (negativo = bajando)
        self.temperature = 300  # K
