import math

class Atmosphere:
    def get_density(self, altitude):
        # Modelo exponencial simplificado
        rho0 = 1.225  # kg/m³ al nivel del mar
        h_scale = 8500  # escala de altura (m)
        return rho0 * math.exp(-altitude / h_scale)